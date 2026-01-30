## Roles

### verify_install
- Installs required service package (using host variable `service_name`).
- Ensures service is enabled and running.
- Uses Ansible facts for status (no shell).
- Reports service state.

### check_disk
- Uses Ansible facts (`ansible_mounts`) to check disk usage.
- Reports if usage exceeds threshold (default 80%).
- Sends alert email to configured address.

### check_status
- Queries REST API endpoint for application health.
- Extracts and reports services that are DOWN.
- Uses structured JSON parsing.

---

## How to Run

### Verify Install
```
ansible-playbook assignment.yml -i inventory -e action=verify_install
```

### Disk Check
```
ansible-playbook assignment.yml -i inventory -e action=check-disk
```

### Status Check
```
ansible-playbook assignment.yml -i inventory -e action=check-status
```
