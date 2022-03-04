# Introduction
This project is to record how to install/deploy kubernetes step by step with ansible

# Installation flow
## Prerequisite[1]:
* Hardware
    * CPU: 2 or more
    * Memory: 2GB or more
* System
    * Unique hostname, mac address, and product uuid for every node
    * Certain ports are open [2]
    * swap disabled in order for kubelet to work properly
    * Make sure that _br_netfilter_ module is loaded
        ```
        In order to:
        1. Enable transparent masquerading
        2. Facilitate VxLAN traffic for communication between k8s pods across the cluster
        ```
# Choices
## container runtime[4]:
* containerd
* CRI-O
* Docker Engine
* Mirantis Container Runtime
```
Based on [5], containerd and cri-o are good choices instead of container
In this project, cri-o will be used for a try
```

## CNI plugin
calico will be chosen

# References
1. https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
2. https://kubernetes.io/docs/reference/ports-and-protocols/
3. https://citizix.com/how-to-set-up-kubernetes-cluster-on-debian-11-with-kubeadm-and-cri-o/
4. https://kubernetes.io/docs/setup/production-environment/container-runtimes/
5. https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd/
6. https://github.com/kubernetes-sigs/kubespray
7. https://kubernetes.io/docs/setup/production-environment/container-runtimes/
8. https://github.com/cri-o/cri-o/blob/main/install.md