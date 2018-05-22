# check_halo_server_config_state

Initiates configuration scan of Halo server by ID, polls until scan is
complete, prints results and exits. This tool exits with non-zero status if
an issue count beyond threshold is detected. Setting any threshold to `-1`
will cause a clean exit, no matter how many issues are discovered.

## Building

`docker build -t check_halo_server_config:latest .`

## Running

```
docker run \
  -it \
  --rm \
  -e HALO_API_KEY=$HALO_API_KEY \
  -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY \
  -e NON_CRITICAL_THRESHOLD=0 \
  -e CRITICAL_THRESHOLD=0 \
  -e SERVER_ID=abc123 \
  check_halo_server_config:latest

```

## Results

```
$ docker run -it --rm -e HALO_API_KEY=$HALO_API_KEY -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY -e SERVER_ID=$HALO_SERVER_ID -e CRITICAL_THRESHOLD=0 -e NON_CRITICAL_THRESHOLD=0 check_halo_server_config:latest

Initiating scan...
Waiting for scan def456 on server abc123 to finish (status queued)
Waiting for scan def456 on server abc123 to finish (status queued)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Waiting for scan def456 on server abc123 to finish (status pending)
Critical: False  Rule: 1.1.10 Ensure separate partition exists for /var/log
Critical: False  Rule: 1.1.11 Ensure separate partition exists for /var/log/audit
Critical: False  Rule: 1.1.12 Ensure separate partition exists for /home
Critical: False  Rule: 1.1.13 Ensure nodev option set on /home partition
Critical: False  Rule: 1.1.14 Ensure nodev option set on /dev/shm partition
Critical: False  Rule: 1.1.15 Ensure nosuid option set on /dev/shm partition
Critical: False  Rule: 1.1.16 Ensure noexec option set on /dev/shm partition
Critical: False  Rule: 1.1.2 Ensure separate partition exists for /tmp
Critical: False  Rule: 1.1.20 Ensure sticky bit is set on all world-writable directories
Critical: False  Rule: 1.1.3 Ensure nodev option set on /tmp partition
Critical: False  Rule: 1.1.4 Ensure nosuid option set on /tmp partition
Critical: False  Rule: 1.1.5 Ensure separate partition exists for /var
Critical: False  Rule: 1.1.6 Ensure separate partition exists for /var/tmp
Critical: False  Rule: 1.1.7 Ensure nodev option set on /var/tmp partition
Critical: False  Rule: 1.1.8 Ensure nosuid option set on /var/tmp partition
Critical: False  Rule: 1.1.9 Ensure noexec option set on /var/tmp partition
Critical: False  Rule: 1.4.1 Ensure permissions on bootloader config are configured
Critical: False  Rule: 1.5.1 Ensure core dumps are restricted
Critical: False  Rule: 1.7.1.4 Ensure permissions on /etc/motd are configured
Critical: False  Rule: 2.2.1.1 Ensure time synchronization is in use
Critical: False  Rule: 2.2.16 Ensure rsync service is not enabled
Critical: False  Rule: 2.3.4 Ensure telnet client is not installed
Critical: False  Rule: 3.1.1 Ensure IP forwarding is disabled
Critical: False  Rule: 3.1.2 Ensure packet redirect sending is disabled
Critical: False  Rule: 3.2.1 Ensure source routed packets are not accepted
Critical: False  Rule: 3.2.2 Ensure ICMP redirects are not accepted
Critical: False  Rule: 3.2.3 Ensure secure ICMP redirects are not accepted
Critical: False  Rule: 3.2.4 Ensure suspicious packets are logged
Critical: False  Rule: 3.3.1 Ensure IPv6 router advertisements are not accepted
Critical: False  Rule: 3.3.2 Ensure IPv6 redirects are not accepted
Critical: False  Rule: 3.4.2 Ensure /etc/hosts.allow is configured
Critical: False  Rule: 3.4.3 Ensure /etc/hosts.deny is configured
Critical: False  Rule: 4.1.2 Ensure auditd service is enabled
Critical: False  Rule: 4.2.1.2 Ensure logging is configured
Critical: False  Rule: 4.2.1.4 Ensure rsyslog is configured to send logs to a remote log host
Critical: False  Rule: 4.2.1.5 Ensure remote rsyslog messages are only accepted on designated log hosts.
Critical: False  Rule: 4.2.2.1 Ensure syslog-ng service is enabled
Critical: False  Rule: 5.1.2 Ensure permissions on /etc/crontab are configured
Critical: False  Rule: 5.1.3 Ensure permissions on /etc/cron.hourly are configured
Critical: False  Rule: 5.1.4 Ensure permissions on /etc/cron.daily are configured
Critical: False  Rule: 5.1.5 Ensure permissions on /etc/cron.weekly are configured
Critical: False  Rule: 5.1.6 Ensure permissions on /etc/cron.monthly are configured
Critical: False  Rule: 5.1.7 Ensure permissions on /etc/cron.d are configured
Critical: False  Rule: 5.1.8 Ensure at/cron is restricted to authorized users
Critical: False  Rule: 5.2.1 Ensure permissions on /etc/ssh/sshd_config are configured
Critical: False  Rule: 5.2.10 Ensure SSH PermitUserEnvironment is disabled
Critical: False  Rule: 5.2.11 Ensure only approved MAC algorithms are used
Critical: False  Rule: 5.2.12 Ensure SSH Idle Timeout Interval is configured
Critical: False  Rule: 5.2.13 Ensure SSH LoginGraceTime is set to one minute or less
Critical: False  Rule: 5.2.14 Ensure SSH access is limited
Critical: False  Rule: 5.2.15 Ensure SSH warning banner is configured
Critical: False  Rule: 5.2.4 Ensure SSH X11 forwarding is disabled
Critical: False  Rule: 5.2.5 Ensure SSH MaxAuthTries is set to 4 or less
Critical: False  Rule: 5.2.8 Ensure SSH root login is disabled
Critical: False  Rule: 5.3.1 Ensure password creation requirements are configured
Critical: False  Rule: 5.3.2 Ensure lockout for failed password attempts is configured
Critical: False  Rule: 5.3.3 Ensure password reuse is limited
Critical: False  Rule: 5.4.1.1 Ensure password expiration is 90 days or less
Critical: False  Rule: 5.4.1.2 Ensure minimum days between password changes is 7 or more
Critical: False  Rule: 5.4.1.4 Ensure inactive password lock is 30 days or less
Critical: False  Rule: 5.4.4 Ensure default user umask is 027 or more restrictive
Critical: False  Rule: 5.6 Ensure access to the su command is restricted
Critical: False  Rule: 6.2.7 Ensure all users' home directories exist
Critical: False  Rule: 6.2.9 Ensure users own their home directories

---
Non-critical findings: 64 Threshold: 0

Threshold exceeded, this job will be marked Failed

$ echo $?
1

```
