## Optimizing Linux before installing Postgresql


This role optimizes linux before moving on to install Postgresql latest version 
on Debian distribution.

The role performs the following steps (in order) 
to optimize Linux before installing latest version
of Postgresql:

- Upgrading Linux kernel 
- Setting/Configuring specific linux kernel parameters
- Installing the latest version of Postgresql

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
here for more details.

## How to Include the role in an audible playbook



