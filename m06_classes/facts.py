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