## Optimizing Linux Servers for Postgres   

![Postgresql](https://www.bing.com/images/blob?bcid=RKbKXw6n7m8CRA)  

Supporting Servers: **Debian** /  **Ubuntu**

There are two main tasks for the optimize_linux
role namely:

- `kernel-linux.yml` task
- `iptables.yml` task

### Kernel-linux Task

The `kernel-linux.yml` optimizes linux before installing Postgresql  
on Debian distribution.

The task performs the following steps (in order) 
to optimize Linux before installing Postgresql.

- Upgrading Linux kernel 
- Setting/Configuring specific linux kernel parameters

You can check here to learn more about these kernel
parameters. 

- SHMMAX: SHMMAX is a kernel parameter 
used to define the maximum size of a single shared
memory segment Linux process can allocate.

- SHMALL : Is another kernel_parameter used to
define system-wide total amount of shared memory
pages.

- Huge Pages: Huge Pages makes it possible for 
Linux to support pages greater than 4KB. Check
[here](https://help.ubuntu.com/community/KVM%20-%20Using%20Hugepages) for more details.

- vm.swappiness: Is another kernel parameter that
is used to control the swapping pages to and from memory 
. 

- vm.overcommit_memory: This memory related parameter is
used by the kernel to allocate memory to application 
running in the userspace.

- vm.overcommit_ratio: This parameter decides the
percentage of RAM available for overloading.

- vm.dirty_background_ratio: Percentage of memory
filled with dirty pages that needs to be written to
disk.  

- vm.dirty_ratio: Similar to `vm.dirty_background_
ratio but needs to contain higher value than the 
preceding kernel parameter.

### iptables Task

If you have forgotten about IP tables rules in Linux,
check [here](https://linux.die.net/man/8/iptables) in order to understand what the task inside the `iptables.yml`  does.  

Variable: `backup_ipaddress` - for allowing specific ip address to backup postgresql using `rsync` service

The `iptables.yml` performs the following:

- Updates systems packages using the `apt` module

-  Then it checks if iptables is already installed 
or not via `package_facts` module. If it's not
installed, then the role installs it via the 
`apt` module. 

- Install `iptables-persistent` package to save iptable rules

- It only allows/accepts packets from port `873` `22` tcp and `5432`. 

- Services allowed `rsync`, `ssh`, `postgres`  

- Then saves current iptables rules to a text file named `iptablerules.txt`  

You can delete the file `iptablerules.txt` after you have copied the file to a remote server.
 
## How to Include the role in an ansible playbook

```
--- 
- hosts: all 
  roles: 
    -  linux-for-postgresql
```

### NB: You need to change the list of default `pg_ipaddress` values to your preferred list of ipaddresses.

Then execute the following command on the terminal
to run the playbook as shown below:

 You can run the role in a playbook by specifying an ipaddress for performing backups via the `backup_ipaddress` variable:
 
`ansible-playbook linux-playbook.yaml --extra-vars "backup_ipaddress=<ip_address>"`  

 Or without any ipaddress for performing backup as shown below: 
 
`ansible-playbook linux-playbook.yaml`  

Also if you want to run the playbook without closing and opening some ports, use the command below:  

`ansible-playbook linux-playbook.yaml skip-tags "iptable"`

The command optimizes linux for postgresql by leaving almost all ports open on linux.    

Finally if you want to set up iptables without optimizing kernel parameters, use the command below: 

`ansible-playbook linux-playbook.yaml skip-tags "always"`  

## Developed By: [Vettabase Ltd](vettabase.com)
