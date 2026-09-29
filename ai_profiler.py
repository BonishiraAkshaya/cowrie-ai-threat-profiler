import json
from collections import defaultdict


log_file ="var/log/cowrie/cowrie.json"


ip_sessions=defaultdict(int)
ip_commands=defaultdict(list)
risk_scores=defaultdict(int)


with open(log_file) as f:
    for line in f:
        try:
            data=json.loads(line)

            if data.get("eventid")=="cowrie.session.connect":
                ip=data.get("src_ip")
                ip_sessions[ip]+=1


            if data.get("eventid")=="cowrie.command.input":
                ip=data.get("src_ip")
                cmd=data.get("input")
                ip_commands[ip].append(cmd)


                if "whoami" in cmd or "uname" in cmd:
                    risk_scores[ip]+=1

                if "cat /etc/passwd" in cmd:
                    risk_scores[ip]+=3

        except:
            continue
print("\n=== AI Threat Report ===\n")


for ip in ip_sessions:
   print("IP:", ip)
   print("Sessions:", ip_sessions[ip])
   print("Commands:",len(ip_commands[ip]))
   print("Risk Score:", risk_scores[ip])
   if risk_scores[ip]>=6:
       level="HIGH"
       action="Auto Block IP (Simulated)"
   elif risk_scores[ip]>=3:
       level="MEDIUM"
       action="Increase Monitoring"
   else:
       level="LOW"
       action="Log Only"

print("Threat Level:", level)
print("Response:", action)
print("-----------------------")
