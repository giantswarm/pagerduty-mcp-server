# pagerduty-mcp-server

PagerDuty MCP Server (Giant Swarm packaging) — exposes the upstream MCP server over HTTP for in-cluster muster integration.

**Homepage:** <https://github.com/giantswarm/pagerduty-mcp-server>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Giant Swarm | <support@giantswarm.io> |  |

## Source Code

* <https://github.com/giantswarm/pagerduty-mcp-server>
* <https://github.com/PagerDuty/pagerduty-mcp-server>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| replicaCount | int | `1` |  |
| image.repository | string | `"gsoci.azurecr.io/giantswarm/pagerduty-mcp-server"` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| nameOverride | string | `"mcp-pagerduty"` |  |
| fullnameOverride | string | `"mcp-pagerduty"` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.automount | bool | `false` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.name | string | `""` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext.runAsNonRoot | bool | `true` |  |
| podSecurityContext.runAsUser | int | `1000` |  |
| podSecurityContext.runAsGroup | int | `1000` |  |
| podSecurityContext.fsGroup | int | `1000` |  |
| podSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| securityContext.allowPrivilegeEscalation | bool | `false` |  |
| securityContext.readOnlyRootFilesystem | bool | `true` |  |
| securityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| service.type | string | `"ClusterIP"` |  |
| service.port | int | `8080` |  |
| service.annotations | object | `{}` |  |
| resources.limits.cpu | string | `"200m"` |  |
| resources.limits.memory | string | `"256Mi"` |  |
| resources.limits.ephemeral-storage | string | `"100Mi"` |  |
| resources.requests.cpu | string | `"50m"` |  |
| resources.requests.memory | string | `"128Mi"` |  |
| resources.requests.ephemeral-storage | string | `"10Mi"` |  |
| livenessProbe.tcpSocket.port | string | `"http"` |  |
| livenessProbe.initialDelaySeconds | int | `5` |  |
| livenessProbe.periodSeconds | int | `10` |  |
| readinessProbe.tcpSocket.port | string | `"http"` |  |
| readinessProbe.initialDelaySeconds | int | `5` |  |
| readinessProbe.periodSeconds | int | `10` |  |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.minReplicas | int | `1` |  |
| autoscaling.maxReplicas | int | `3` |  |
| autoscaling.targetCPUUtilizationPercentage | int | `80` |  |
| nodeSelector | object | `{}` |  |
| tolerations | list | `[]` |  |
| affinity | object | `{}` |  |
| ciliumNetworkPolicy.enabled | bool | `false` |  |
| mcp.transport | string | `"streamable-http"` |  |
| mcp.host | string | `"0.0.0.0"` |  |
| mcp.port | int | `8080` |  |
| mcp.enableWriteTools | bool | `false` |  |
| pagerduty.apiHost | string | `"https://api.eu.pagerduty.com"` |  |
| pagerduty.existingSecret.name | string | `"pagerduty-mcp"` |  |
| pagerduty.existingSecret.key | string | `"apiKey"` |  |
