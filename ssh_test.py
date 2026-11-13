
import paramiko

# Host server configuration
HOST = "172.31.46.52"
USERNAME = "ec2-user"
KEY_FILE = "/root/.ssh/id_ed25519"

# Create SSH client
ssh = paramiko.SSHClient()

# Load trusted SSH host keys
ssh.load_system_host_keys()

try:
    print("Connecting to Host Server...")

    ssh.connect(
        hostname=HOST,
        username=USERNAME,
        key_filename=KEY_FILE,
        port=22,
        timeout=10
    )

    print("SSH Connection: SUCCESS")

    # Execute command on remote host
    stdin, stdout, stderr = ssh.exec_command("hostname")

    remote_hostname = stdout.read().decode().strip()

    print("Remote Hostname:", remote_hostname)

    print("Remote command executed successfully!")

except Exception as error:
    print("SSH Connection Failed:", error)

finally:
    ssh.close()

