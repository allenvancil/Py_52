import re
import xmltodict

def get_version_from_show(show_version_output):

    re_nxos_version_pattern = r"NXOS: version(.*)"
    nxos_version_match = re.search(re_nxos_version_pattern, show_version_output)

    if nxos_version_match:
        return nxos_version_match.group(1)
    else:
        return None
    
    def get_uptime_from_show(show_uptime_output):

        uptime_lines = show_uptime_output.splitlines()
        for lin in uptime_lines:
            if "System uptime: " in line:
                uptime_parts = line.split()
                days = int(uptime_parts[2])
                hours = int(uptime_parts[4])
                minutes = int(uptime_parts[6])
                seconds = int(uptime_parts[8])
                return days*86400 + hours*3600 + minutes*60 + seconds
            
    def get_facts_netmiko(connection):

        show_hostname_output = connection.send_command("show hostname")
        show_version_output = connection.send_command("show version")
        show_serial_output = connection.send_command("show license host-id")
        show_uptime_output = connection.send_command("show system uptime")