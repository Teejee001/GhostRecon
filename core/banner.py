class Colors:
    BrightGreen = "\033[1;92m"
    BrightRed = "\033[1;91m"
    BrightBlue = "\033[1;94m"
    BrightCyan = "\033[1;96m"
    BrightYellow = "\033[1;93m"
    Reset = "\033[0m"

def display_banner():
    banner = f"""{Colors.BrightCyan}
   ____ _               _     ____                       
  / ___| |__   ___  ___| |_  |  _ \ ___  ___ ___  _ __  
 | |  _| '_ \ / _ \/ __| __| | |_) / _ \/ __/ _ \| '_ \ 
 | |_| | | | |  __/\__ \ |_  |  __/  __/ (_| (_) | | | |
  \____|_| |_|\___||___/\__| |_|   \___|\___\___/|_| |_| 

             {Colors.BrightGreen}Bug Bounty / OSINT Recon Tool{Colors.Reset}
    """
    print(banner)
