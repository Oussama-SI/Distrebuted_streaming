### diferent K8s apiVersion & kind types:

| `apiVersion`                   | `kind`                               | Purpose                   |
| ------------------------------ | ------------------------------------ | ------------------------- |
| `v1`                           | `Pod`                                | Smallest deployable unit  |
| `v1`                           | `Service`                            | Expose Pods on a network  |
| `v1`                           | `ConfigMap`                          | Inject config into apps   |
| `v1`                           | `Secret`                             | Inject sensitive data     |
| `v1`                           | `PersistentVolume`                   | Abstraction for storage   |
| `v1`                           | `PersistentVolumeClaim`              | Request storage           |
| `apps/v1`                      | `Deployment`                         | Manage pod rollout        |
| `apps/v1`                      | `StatefulSet`                        | Manage stateful apps      |
| `apps/v1`                      | `DaemonSet`                          | Run on every node         |
| `batch/v1`                     | `Job`                                | Run one-off tasks         |
| `batch/v1`                     | `CronJob`                            | Run jobs on a schedule    |
| `autoscaling/v2`               | `HorizontalPodAutoscaler`            | Auto-scale pods           |
| `networking.k8s.io/v1`         | `Ingress`                            | HTTP routing to services  |
| `rbac.authorization.k8s.io/v1` | `Role` / `ClusterRole`               | Define permissions        |
| `rbac.authorization.k8s.io/v1` | `RoleBinding` / `ClusterRoleBinding` | Grant permissions         |
| `policy/v1`                    | `PodDisruptionBudget`                | Control pod eviction      |
| `apiextensions.k8s.io/v1`      | `CustomResourceDefinition` (CRD)     | Define your own API types |
| `coordination.k8s.io/v1`       | `Lease`                              | Used in leader election   |
