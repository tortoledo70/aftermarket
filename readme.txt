    ___    ______                                 __        __
   /   |  / __/ /____  _________ ___  ____ ______/ /_____  / /_    
  / /| | / /_/ __/ _ \/ ___/ __ `__ \/ __ `/ ___/ //_/ _ \/ __/    
 / ___ |/ __/ /_/  __/ /  / / / / / / /_/ / /  / ,< /  __/ /_      
/_/  |_/_/  \__/\___/_/  /_/ /_/ /_/\__,_/_/  /_/|_|\___/\__/




< About >

    > aftermarket.py was written to automate the process of installing an arsenal of tools used for pentesting.

< Usage >

    > You can clone the aftermarket repository with the following command:
        
       >> git clone https://github.com/K0FIN/aftermarket.git

    > To use, simply run the script:
    
       >> python aftermarket.py

< Process >
    
    > The script is written to be executed in the "/root" path. 
      The script will be aborted if it is executed anywhere else.
       
    > Once the script is executed, you will be given a list of what the script will do, which looks like the following:

        >> Update the root password (prompted for change with 'passwd')
        >> Update system repositories.
        >> Update system distribution.
        >> Start the Postgresql service.
        >> Start the Metasploit service.
        >> Prompt for enabling Metasploit logging.
        >> Prompt for enabling Metasploit and Postgresql services at start up.

    > You will also be shown what tools are being installed:

        >> Discover Scripts
        >> Smbexec
        >> Veil
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
        >> Extra Tools (named gitlist, this is a HUGE repo of tools to add to your arsenal).

    > After the tools are installed, you will be given a list of tools that have to be download via browser.
    > This list will be shown in STDOUT as well as written to a text file called browser_links.txt for later use.


< Why It's Written>

    > After reading The Hacker Playbook, written by Peter Kim, I had found value in the setup phase at the beginning
      of the book. This phase illustrated to the reader how they should set up their fresh installation of Kali Linux. 
      The reader is walked through updating their password to something more secure to upgrading their distro, and 
      continuing on to installing tools and useful resources that show value in a pentest, according to the book.
      
      Since reading this, I had found it useful to use the tools and settings described in the setup phase 
      of the book as the baseline for my new installations of Kali Linux, regardless of whether or not I would be following
      anything in the book. So, one night after installing a new Kali Linux image, I pulled the book out to update the configurations and 
      install the extra tools shown within it, but the last thing I wanted to do at that time was to manually follow every single cloned repository
      and shell command shown. I thought to myself, "Man, it would be great if someone automated this. You'd think, with
      as many people as there are in the industry who have purchased or read this book that someone would have written a script
      to automate all of this stuff." At that point, I decided to do it myself, especially since I had just installed a new
      Kali image that I could easily test my code on. One-and-a-half hours or so later, with a whole lot of tool sources shown in the book
      plus a chunk of simple Python code and a little bit of color, I had a finished script.

      Hopefully, others find value from this simple automated task. There are, of course, other auto-oriented scripts out there for
      things like this, such as Lazykali. However, my goal was not to create an interactive-oriented tool that presents a whole lot
      of options. I simply needed to automate the tasks required to install these tools to my system, and that is exactly what this script does.

< Credit >

    > I'd like to recognize Peter Kim for the information he provided within his book. This script probably would not have been written otherwise.
      I highly recommend it to anyone involved in pentesting, regardless of skill level. You can purchase it on Amazon (http://www.amazon.com/dp/1494932636),
      and you can find the updates to the book at The Hacker Playbook website (http://www.thehackerplaybook.com/updates).

    > I'd like to give credit to Dr. Dinosaur for providing practical suggestions regarding the functionality of the code and the experience of the end user.
