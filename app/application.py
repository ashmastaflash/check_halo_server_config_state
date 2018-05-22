import cloudpassage
import os
import sys
import time


def main():
    # Set up config and Halo objects.
    config = cloudpassage.ApiKeyManager()
    server_id = os.getenv("SERVER_ID")
    crit_threshold = int(os.getenv("CRITICAL_THRESHOLD"))
    non_crit_threshold = int(os.getenv("NON_CRITICAL_THRESHOLD"))
    halo_session = cloudpassage.HaloSession(config.key_id, config.secret_key,
                                            api_host=config.api_hostname)
    server_obj = cloudpassage.Server(halo_session)
    scan_obj = cloudpassage.Scan(halo_session)
    # Initiate a scan of the target server
    print("Initiating scan...")
    job_id = scan_obj.initiate_scan(server_id, 'sca')["id"]
    incomplete_statuses = ["queued", "pending", "running"]
    scan_status = "queued"
    while scan_status in incomplete_statuses:
        time.sleep(20)
        print("Waiting for scan %s on server %s to finish (status %s)" % (job_id, server_id, scan_status))  # NOQA
        scan_status = server_obj.command_details(server_id, job_id)["status"]
    scan_results = scan_obj.last_scan_results(server_id, 'sca')["scan"]
    over_threshold = False
    threshold_msg = ""
    crit_findings = scan_results["critical_findings_count"]
    non_crit_findings = scan_results["non_critical_findings_count"]
    # Test criticality against threshold
    if crit_findings > crit_threshold:
        threshold_msg += "Critical findings: %s Threshold: %s\n" % (crit_findings, crit_threshold)  # NOQA
        if crit_threshold != -1:
            over_threshold = True
        else:
            threshold_msg += "Critical threshold set to -1, not failing.\n"
    if non_crit_findings > non_crit_threshold:
        threshold_msg += "Non-critical findings: %s Threshold: %s\n" % (non_crit_findings, crit_threshold)  # NOQA
        if non_crit_threshold != -1:
            over_threshold = True
        else:
            threshold_msg += "Non-critical threshold set to -1, not failing.\n"
    # Build findings text
    failed_items = ""
    bad_findings = [f for f in scan_results["findings"] if f["status"] == 'bad']  # NOQA
    for finding in bad_findings:
        msg = "Critical: %s  Rule: %s\n" % (str(finding["critical"]),
                                            finding["rule_name"])
        failed_items += msg
    output_msg = "\n---\n".join([failed_items, threshold_msg])
    print(output_msg)
    # Exit with 1 if we are over threshold.
    if over_threshold:
        print("Threshold exceeded, this job will be marked Failed")
        sys.exit(1)
    else:
        print("Nothing exceeds thresholds; this job will be marked Passed.")


if __name__ == "__main__":
    main()
