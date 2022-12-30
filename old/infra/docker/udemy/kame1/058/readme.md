# How to limit host resource
- `--cpus x`
  - x specifies the numbrer of cpu cores
- `--memory x`
  - x speficies the memory size


## TEST
- run
```bash
>>>  docker run -it --rm --cpus 1 --memory 1g ubuntu bash
root@e6644ccbcba9:/#
```

- Make a confirmation
  - <details>
    <summary>all</summary>

    ```json
    ~ >>> docker inspect e6644ccbcba9
    [
        {
            "Id": "e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381",
            "Created": "2021-01-04T10:17:20.15926027Z",
            "Path": "bash",
            "Args": [],
            "State": {
                "Status": "running",
                "Running": true,
                "Paused": false,
                "Restarting": false,
                "OOMKilled": false,
                "Dead": false,
                "Pid": 9830,
                "ExitCode": 0,
                "Error": "",
                "StartedAt": "2021-01-04T10:17:20.850564663Z",
                "FinishedAt": "0001-01-01T00:00:00Z"
            },
            "Image": "sha256:f643c72bc25212974c16f3348b3a898b1ec1eb13ec1539e10a103e6e217eb2f1",
            "ResolvConfPath": "/var/lib/docker/containers/e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381/resolv.conf",
            "HostnamePath": "/var/lib/docker/containers/e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381/hostname",
            "HostsPath": "/var/lib/docker/containers/e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381/hosts",
            "LogPath": "/var/lib/docker/containers/e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381/e6644ccbcba97b47fe62316594fd512956a6974be6057046310f346e1b779381-json.log",
            "Name": "/nifty_hodgkin",
            "RestartCount": 0,
            "Driver": "overlay2",
            "Platform": "linux",
            "MountLabel": "",
            "ProcessLabel": "",
            "AppArmorProfile": "",
            "ExecIDs": null,
            "HostConfig": {
                "Binds": null,
                "ContainerIDFile": "",
                "LogConfig": {
                    "Type": "json-file",
                    "Config": {}
                },
                "NetworkMode": "default",
                "PortBindings": {},
                "RestartPolicy": {
                    "Name": "no",
                    "MaximumRetryCount": 0
                },
                "AutoRemove": true,
                "VolumeDriver": "",
                "VolumesFrom": null,
                "CapAdd": null,
                "CapDrop": null,
                "Capabilities": null,
                "Dns": [],
                "DnsOptions": [],
                "DnsSearch": [],
                "ExtraHosts": null,
                "GroupAdd": null,
                "IpcMode": "private",
                "Cgroup": "",
                "Links": null,
                "OomScoreAdj": 0,
                "PidMode": "",
                "Privileged": false,
                "PublishAllPorts": false,
                "ReadonlyRootfs": false,
                "SecurityOpt": null,
                "UTSMode": "",
                "UsernsMode": "",
                "ShmSize": 67108864,
                "Runtime": "runc",
                "ConsoleSize": [
                    0,
                    0
                ],
                "Isolation": "",
                "CpuShares": 0,
                "Memory": 1073741824,
                "NanoCpus": 1000000000,
                "CgroupParent": "",
                "BlkioWeight": 0,
                "BlkioWeightDevice": [],
                "BlkioDeviceReadBps": null,
                "BlkioDeviceWriteBps": null,
                "BlkioDeviceReadIOps": null,
                "BlkioDeviceWriteIOps": null,
                "CpuPeriod": 0,
                "CpuQuota": 0,
                "CpuRealtimePeriod": 0,
                "CpuRealtimeRuntime": 0,
                "CpusetCpus": "",
                "CpusetMems": "",
                "Devices": [],
                "DeviceCgroupRules": null,
                "DeviceRequests": null,
                "KernelMemory": 0,
                "KernelMemoryTCP": 0,
                "MemoryReservation": 0,
                "MemorySwap": 2147483648,
                "MemorySwappiness": null,
                "OomKillDisable": false,
                "PidsLimit": null,
                "Ulimits": null,
                "CpuCount": 0,
                "CpuPercent": 0,
                "IOMaximumIOps": 0,
                "IOMaximumBandwidth": 0,
                "MaskedPaths": [
                    "/proc/asound",
                    "/proc/acpi",
                    "/proc/kcore",
                    "/proc/keys",
                    "/proc/latency_stats",
                    "/proc/timer_list",
                    "/proc/timer_stats",
                    "/proc/sched_debug",
                    "/proc/scsi",
                    "/sys/firmware"
                ],
                "ReadonlyPaths": [
                    "/proc/bus",
                    "/proc/fs",
                    "/proc/irq",
                    "/proc/sys",
                    "/proc/sysrq-trigger"
                ]
            },
            "GraphDriver": {
                "Data": {
                    "LowerDir": "/var/lib/docker/overlay2/a617d4b7a1b33b7cebb47e0419b77ca5cb20ddd46265a271cff05e8b021dfa1f-init/diff:/var/lib/docker/overlay2/e1c8c898a2e3ce34a7c283d4dad5250cc43f59a7d2209786db761450a04d8fcb/diff:/var/lib/docker/overlay2/ba208b1c5ff7a54ee4e7b8d2086442abe55c9c14a94f635f05144beb2379afeb/diff:/var/lib/docker/overlay2/fd338fff5f330508e2b0ce63f3ad205a86e8bc811e065835c2b15af35b339fc9/diff",
                    "MergedDir": "/var/lib/docker/overlay2/a617d4b7a1b33b7cebb47e0419b77ca5cb20ddd46265a271cff05e8b021dfa1f/merged",
                    "UpperDir": "/var/lib/docker/overlay2/a617d4b7a1b33b7cebb47e0419b77ca5cb20ddd46265a271cff05e8b021dfa1f/diff",
                    "WorkDir": "/var/lib/docker/overlay2/a617d4b7a1b33b7cebb47e0419b77ca5cb20ddd46265a271cff05e8b021dfa1f/work"
                },
                "Name": "overlay2"
            },
            "Mounts": [],
            "Config": {
                "Hostname": "e6644ccbcba9",
                "Domainname": "",
                "User": "",
                "AttachStdin": true,
                "AttachStdout": true,
                "AttachStderr": true,
                "Tty": true,
                "OpenStdin": true,
                "StdinOnce": true,
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "Cmd": [
                    "bash"
                ],
                "Image": "ubuntu",
                "Volumes": null,
                "WorkingDir": "",
                "Entrypoint": null,
                "OnBuild": null,
                "Labels": {}
            },
            "NetworkSettings": {
                "Bridge": "",
                "SandboxID": "b9d8a32074fb394b2c209e53e77f2d5cd4fc2ff20aefd0c46421684abd693637",
                "HairpinMode": false,
                "LinkLocalIPv6Address": "",
                "LinkLocalIPv6PrefixLen": 0,
                "Ports": {},
                "SandboxKey": "/var/run/docker/netns/b9d8a32074fb",
                "SecondaryIPAddresses": null,
                "SecondaryIPv6Addresses": null,
                "EndpointID": "f3ddf28fef01da85434ce7200e8d2d8084eca9abdb5f354df4dea2479cfa63f6",
                "Gateway": "172.17.0.1",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "IPAddress": "172.17.0.3",
                "IPPrefixLen": 16,
                "IPv6Gateway": "",
                "MacAddress": "02:42:ac:11:00:03",
                "Networks": {
                    "bridge": {
                        "IPAMConfig": null,
                        "Links": null,
                        "Aliases": null,
                        "NetworkID": "66ef382fcab982a5714f193ebed2fbaac2d9420449132fd8d6d4a5918a8e3022",
                        "EndpointID": "f3ddf28fef01da85434ce7200e8d2d8084eca9abdb5f354df4dea2479cfa63f6",
                        "Gateway": "172.17.0.1",
                        "IPAddress": "172.17.0.3",
                        "IPPrefixLen": 16,
                        "IPv6Gateway": "",
                        "GlobalIPv6Address": "",
                        "GlobalIPv6PrefixLen": 0,
                        "MacAddress": "02:42:ac:11:00:03",
                        "DriverOpts": null
                    }
                }
            }
        }
    ]
    ~ >>
    ```
    </details>
  - <details>
    <summary>grep cpu</summary>
    
    ```json
    ~ >>> docker inspect e6644ccbcba9 | grep -i cpu
            "CpuShares": 0,
            "NanoCpus": 1000000000,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "CpuCount": 0,
            "CpuPercent": 0,
    ~ >>>
    ```
    </details>
  - <details>
    <summary>grep memory</summary>
    
    ```json
    ~ >>> docker inspect e6644ccbcba9 | grep -i mem
                "Memory": 1073741824,
                "CpusetMems": "",
                "KernelMemory": 0,
                "KernelMemoryTCP": 0,
                "MemoryReservation": 0,
                "MemorySwap": 2147483648,
                "MemorySwappiness": null,
    ~ >>>
    ```
    </details>
