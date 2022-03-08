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
## Flow
1. Check if each node has unique mac address, product uuid, and hostname
2. disable swap
3. Check relevant kernel modules loaded
    * br_netfilter
    * overlay
4. Install kubelet, kubeadm and kubectl
5. Install container runtime
6. Initialize master node
    * enable the kubelet service to start on boot
    * pull the required images with kubeadmin
    * execute 'kubeadmin init ...'
7. On master node, copy /etc/kubernetes/admin.conf to $HOME/.kube or set to KUBECONFIG environment
8. Install CNI
9. Join worker nodes
```
Join nodes: kubeadm join --token <token> <control-plane-host>:<control-plane-port> --discovery-token-ca-cert-hash sha256:<hash>
token can get from 'kubeadm token list'
hash can get by executing:
    openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | \
   openssl dgst -sha256 -hex | sed 's/^.* //'

If token expired (24 hours by default), generate it by 'kubeadm token create'
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
calico [9] will be chosen
If pod network CIDR is not set as 192.168.0.0, download custom-resources.yaml and alter it

# References
1. https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
2. https://kubernetes.io/docs/reference/ports-and-protocols/
3. https://citizix.com/how-to-set-up-kubernetes-cluster-on-debian-11-with-kubeadm-and-cri-o/
4. https://kubernetes.io/docs/setup/production-environment/container-runtimes/
5. https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd/
6. https://github.com/kubernetes-sigs/kubespray
7. https://kubernetes.io/docs/setup/production-environment/container-runtimes/
8. https://github.com/cri-o/cri-o/blob/main/install.md
9. https://projectcalico.docs.tigera.io/getting-started/kubernetes/quickstart