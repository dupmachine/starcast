import json
import os
import sys
import urllib.request

servers = [s.strip() for s in os.environ['SERVERS'].strip().splitlines() if s.strip()]

if not servers:
    print('')
    sys.exit(0)

mcp_servers = {}
for server_name in servers:
    url = f"https://registry.smithery.ai/servers/{server_name}"
    try:
        req = urllib.request.urlopen(url, timeout=10)
        data = json.loads(req.read())
    except Exception as e:
        print(f"Warning: could not fetch {server_name}: {e}", file=sys.stderr)
        continue

    connections = data.get('connections', [])
    http_conn = next((c for c in connections if c.get('type') == 'http'), None)
    if not http_conn:
        print(f"Warning: no HTTP connection for {server_name}", file=sys.stderr)
        continue

    deployment_url = http_conn['deploymentUrl']
    config_schema = http_conn.get('configSchema', {})

    # Use ${VAR} placeholders — resolved by claude-code-action from its env
    # Example: ?TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}&TELEGRAM_CHANNEL_ID=${TELEGRAM_CHANNEL_ID}
    params = [f"{prop}=${{{prop}}}" for prop in config_schema.get('properties', {})]
    full_url = f"{deployment_url}?{'&'.join(params)}" if params else deployment_url

    key = server_name.split('/')[-1]
    mcp_servers[key] = {"type": "http", "url": full_url}

print(json.dumps({"mcpServers": mcp_servers}) if mcp_servers else '')
