#!/usr/bin/python

import os
import sys


#Before anything else, let's check to make sure that we are running the script from the proper path.
if os.path.realpath(__file__) != '/root/aftermarket.py':
    print "\033[1;31m[!]\033[1;m\033[1;37mERROR! This script must be run from the /root path of the filesystem.\033[1;m"
    sys.exit()
else:
    pass

external_link_file = open('/root/browser_links.txt','w')
os.system('clear')

print "\033[1;37m=\033[1;m" * 95
print """\033[1;34m
    ___    ______                                 __        __     
   /   |  / __/ /____  _________ ___  ____ ______/ /_____  / /_    
  / /| | / /_/ __/ _ \/ ___/ __ `__ \/ __ `/ ___/ //_/ _ \/ __/    
 / ___ |/ __/ /_/  __/ /  / / / / / / /_/ / /  / ,< /  __/ /_      
/_/  |_/_/  \__/\___/_/  /_/ /_/ /_/\__,_/_/  /_/|_|\___/\__/\033[1;m\033[1;37m

aftermarket.py | Automated pentesting tool installation for Kali Linux
               | Written by Kory Findley (K0FIN)
\033[1;m
"""                                                                   
print "\033[1;37m=\033[1;m" * 95

print """\033[1;32m
[*]\033[1;m\033[1;37mAftermarket will perform the following actions on your system:
  >> Update the root password (prompted for change with 'passwd')
  >> Update system repositories.
  >> Update system distribution.
  >> Update system packages.
  >> Start the Postgresql service.
  >> Start the Metasploit service.
  >> Prompt for enabling Metasploit logging.
  >> Prompt for enabling Metasploit and Postgresql services on startup.\033[1;m

\033[1;32m[*]\033[1;m\033[1;37mAftermarket will install the following tools on your system:
  >> Discover Scripts
  >> Smbexec
  >> Veil Evasion
  >> Windows Credential Editor
  >> Mimikatz
  >> rockyou.txt wordlist
  >> Peepingtom
  >> banner-plus.nse Nmap Script
  >> PowerSploit
  >> Responder
  >> Social Engineering Toolkit
  >> BypassUAC
  >> BeEF
  >> Burp Suite Fuzzing Lists
  >> Extra Tools (named gitlist, this is a HUGE repo of tools to add to your arsenal).\033[1;m
"""

start = raw_input('\033[1;32m[*]\033[1;m\033[1;37mWould you like to continue? (Y / n): \033[1;m')
if start == "Y" or start == "YES" or start == "Yes" or start == "yes" or start == "y" or start == "":
    pass
else:
    print "\033[1;31m[!]\033[1;m\033[1;37mAftermarket Aborted!\033[1;m"
    sys.exit()

print "\033[1;32m[*]\033[1;m\033[1;37mStarting root password update:\033[1;m"
os.system('passwd')

print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mUpdating repositories...\033[1;m"
os.system('apt-get update')

print "\033[1;32m[*]\033[1;m\033[1;37mUpdating distribution...\033[1;m"
os.system('apt-get dist-upgrade && apt-get upgrade')

print "\033[1;32m[*]\033[1;m\033[1;37mStarting Metasploit Services...\033[1;m"
os.system('service postgresql start')
os.system('service metasploit start')

metasploit_log = raw_input("\033[1;32m[*]\033[1;m\033[1;37mEnable Logging for Metasploit? (Y / N): \033[1;m")
if metasploit_log == "Y" or metasploit_log == "YES" or metasploit_log == "Yes" or metasploit_log == "yes" or metasploit_log == "y" or metasploit_log == "":
    os.system('echo "spool /root/msf_console.log" > /root/.msf4/msfconsole.rc')
else:
    print "\033[1;32m[*]\033[1;m\033[1;37mLogging not enabled.\033[1;m"
    print "\033[1;32m[*]\033[1;m\033[1;37mYou can enable this option later by executing the following command:\033[1;m"
    print ""
    print '\033[1;37mecho "spool /root/msf_console.log" > /root/.msf4/msfconsole.rc\033[1;m'

print ""
raw_input("\033[1;32m[*]\033[1;m\033[1;37mPress ENTER to continue-\033[1;m")
metasploit_startup = raw_input("\033[1;32m[*]\033[1;m\033[1;37mEnable Services on Startup for Metasploit? (Y / N)\033[1;m")
if metasploit_startup == "Y" or metasploit_startup == "YES" or metasploit_startup == "Yes" or metasploit_startup == "yes" or metasploit_startup == "y" or metasploit_startup == "":
    os.system('update-rc.d metasploit enable')
    os.system('update-rc.d postgresql enable')
else:
    print "\033[1;32m[*]\033[1;m\033[1;37mServices not enabled on startup.\033[1;m"
    print "\033[1;32m[*]\033[1;m\033[1;37mYou can enable boot-time service start up later with the following commands:\033[1;m"
    
    print ""
    print '\033[1;37mupdate-rc.d postgresql enable\033[1;m'
    print '\033[1;37mupdate-rc.d metasploit enable\033[1;m'
    print ""
    raw_input("\033[1;32m[*]\033[1;m\033[1;37mPress\033[1;m\033[1;33m[ENTER]\033[1;m")
    
print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Discover Scripts...\033[1;m"
os.system('cd /opt && git clone https://github.com/leebaird/discover.git && cd discover && ./setup.sh')
print "\033[1;32m[*]\033[1;m\033[1;37mDiscover Scripts Installed.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Smbexec...\033[1;m"
os.system('cd /opt && git clone https://github.com/pentestgeek/smbexec.git')
print "\033[1;32m[*]\033[1;m\033[1;37mWhen prompted during the following install script for smbexec, use the following options:\033[1;m"
print "\033[1;37m  >> Select number 1.\033[1;m"
print "\033[1;37m  >> Press ENTER for default value (/opt).\033[1;m"
raw_input("\033[1;32m[*]\033[1;m\033[1;37mPress\033[1;m\033[1;33m[ENTER]\033[1;m")
os.system('cd /opt/smbexec && ./install.sh')

print "\033[1;32m[*]\033[1;m\033[1;37mWhen prompted during the following install script for smbexec (this is the second time it is executed), use the following options-\033[1;m"  
print "\033[1;37m  >> Select number 4 (to compile smbexec).\033[1;m"
print "\033[1;37m  >> After smbexec is compiled and you are returned to the main menu, select number 5 to exit.\033[1;m"
raw_input("\033[1;32m[*]\033[1;m\033[1;37mPress\033[1;m\033[1;33m[ENTER]\033[1;m")
os.system('cd /opt/smbexec && ./install.sh')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Veil Evasion...\033[1;m"
os.system('cd /opt && git clone https://github.com/veil-evasion/Veil.git && cd Veil/setup && ./setup.sh')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Windows Credential Editor (WCE)...\033[1;m"
os.system('cd ~/Desktop && wget http://www.ampliasecurity.com/research/wce_v1_41beta_universal.zip && unzip -d ./wce wce_v1_41beta_universal.zip')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Mimikatz...\033[1;m"
os.system('cd ~/Desktop && wget http://blog.gentilkiwi.com/downloads/mimikatz_trunk.zip && unzip -d ./mimikatz mimikatz_trunk.zip')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling rockyou.txt wordlist...\033[1;m"
os.system('cd ~/Desktop && mkdir password_list && cd password_list && wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2 && bzip2 -d rockyou.txt.bz2')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Peepingtom...\033[1;m"
os.system('cd /opt && wget http://thehackerplaybook.com/Download/peepingtom.zip && unzip peepingtom.zip && cd peepingtom && chmod +x *')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling banner-plus.nse Nmap script...\033[1;m"
os.system('cd /usr/share/nmap/scripts && wget https://raw.github.com/hdm/scan-tools/master/nse/banner-plus.nse')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling PowerSploit...\033[1;m"
os.system('cd /opt && git clone https://github.com/mattifestation/PowerSploit.git && cd PowerSploit && wget https://raw.github.com/obscuresec/random/master/StartListener.py && wget https://raw.github.com/darkoperator/powershell_scripts/master/ps_encoder.py')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Responder...\033[1;m"
os.system('cd /opt && git clone https://github.com/SpiderLabs/Responder.git')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Social Engineering Toolkit (SET)...\033[1;m"
os.system('cd /opt && git clone https://github.com/trustedsec/social-engineer-toolkit.git set/ && cd set && python setup.py install')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling bypassuac...\033[1;m"
os.system('cd /opt && wget http://www.trustedsec.com/files/bypassuac.zip && unzip bypassuac.zip')
os.system('cp /opt/bypassuac/bypassuac.rb /opt/metasploit/apps/pro/msf3/scripts/meterpreter/')
os.system('mv /opt/bypassuac/uac/ /opt/metasploit/apps/pro/msf3/data/exploits/')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling BeEF...\033[1;m"
os.system('apt-get install beef-xss')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling fuzzing lists for Burp Suite...\033[1;m"
os.system('cd /opt && git clone https://github.com/danielmiessler/SecLists.git')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

print "\033[1;32m[*]\033[1;m\033[1;37mInstalling Extra Tools (Gitlist)...\033[1;m"
os.system('cd /opt && mkdir gitlist && cd gitlist && git clone https://github.com/macubergeek/gitlist.git && cd gitlist && chmod +x gitlist.sh && ./gitlist.sh')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"
print ""
print "\033[1;32m[*]\033[1;m\033[1;37mTool installation is complete. The following recommended tools should be downloaded and installed via browser:\033[1;m"
print ""
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37mCrackstation Human Only Wordlist (3 Optional Sites)\033[1;37m"
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37m  >> https://mega.co.nz/#!VIwSmYhL!Q_u0io3nSxIeVnquONJcfb7D7aO0_fpi9SxSchR1mTM\033[1;m"
print "\033[1;37m  >> http://www.filedropper.com/crackstation-human-onlytxt\033[1;m"
print "\033[1;37m  >> https://www.dropbox.com/s/ucreldsa3qt1rms/crackstation-human-only.txt.gz?dl=0\033[1;m"
print "\033[1;34m=\033[1;m" * 95
print "\033[1;34m-\033[1;m" * 95
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37mBurpsuite\033[1;m"
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37m  >> http://portswigger.net/burp/proxy.html\033[1;m"
print "\033[1;34m=\033[1;m" * 95
print "\033[1;34m-\033[1;m" * 95
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37mFirefox Add-Ons\033[1;m"
print "\033[1;34m=\033[1;m" * 95
print "\033[1;37m  Web Dev Add-On      >>  https://addons.mozilla.org/en-US/firefox/addon/web-developer/\033[1;m"
print "\033[1;37m  Tamper Data         >>  https://addons.mozilla.org/en-US/firefox/addon/tamper-data/\033[1;m"
print "\033[1;37m  Foxy Proxy          >>  https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/\033[1;m"
print "\033[1;37m  User Agent Switcher >>  https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/\033[1;m"
print "\033[1;34m=\033[1;m" * 95

print "\033[1;32m[*]\033[1;m\033[1;37mWriting browser-downloadable tool links to file (/root/browser_links.txt)...\033[1;m"

external_link_file.write("=" * 95 + '\n')
external_link_file.write("Crackstation Human Only Wordlist (Various links)\n")
external_link_file.write("=" * 95 + '\n')
external_link_file.write("  >> https://mega.co.nz/#!VIwSmYhL!Q_u0io3nSxIeVnquONJcfb7D7aO0_fpi9SxSchR1mTM\n")
external_link_file.write("  >> http://www.filedropper.com/crackstation-human-onlytxt\n")
external_link_file.write("  >> https://www.dropbox.com/s/ucreldsa3qt1rms/crackstation-human-only.txt.gz?dl=0\n")
external_link_file.write("=" * 95 + '\n')
external_link_file.write("-" * 95 + '\n')
external_link_file.write("=" * 95 + '\n')
external_link_file.write("Burpsuite\n")
external_link_file.write("=" * 95 + '\n')
external_link_file.write("  >> http://portswigger.net/burp/proxy.html\n")
external_link_file.write("=" * 95 + '\n')
external_link_file.write("-" * 95 + '\n')
external_link_file.write("=" * 95 + '\n')
external_link_file.write("Firefox Add-Ons\n")
external_link_file.write("=" * 95 + '\n')
external_link_file.write("  Web Dev Add-On      >>  https://addons.mozilla.org/en-US/firefox/addon/web-developer/\n")
external_link_file.write("  Tamper Data         >>  https://addons.mozilla.org/en-US/firefox/addon/tamper-data/\n")
external_link_file.write("  Foxy Proxy          >>  https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/\n")
external_link_file.write("  User Agent Switcher >>  https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/\n")
external_link_file.write("=" * 95)
external_link_file.close()

print "\033[1;32m[*]\033[1;m\033[1;37mFile written.\033[1;m"
print "\033[1;32m[*]\033[1;m\033[1;37mRemoving zip files...\033[1;m"
os.system('cd /opt && rm peepingtom.zip && rm bypassuac.zip')
os.system('cd ~/Desktop && rm wce_v1_41beta_universal.zip')
os.system('cd ~/Desktop && rm mimikatz_trunk.zip')
print "\033[1;32m[*]\033[1;m\033[1;37mDone.\033[1;m"

os.system('cd ~')
raw_input("\033[1;36m[+]\033[1;m\033[1;37mAftermarket finished. Press\033[1;m\033[1;33m[ENTER]\033[1;m")
sys.exit()
