#!/c/envs/cgi/python

# Wrapper to run Houdini with custom environment
import os, subprocess, sys

#sys.path.append("C:/Program Files/Side Effects Software/Houdini 18.0.287/houdini/python2.7libs")

houdini = 'C:/Program Files/Side Effects Software/Houdini 21.0.596/bin/houdinifx.exe'

#PROJECT_HOME = "h:/HOU"
#os.environ['HOME'] = '{}'.format(PROJECT_HOME)

#os.environ["SHOW"] = "RFO"

# Add Arnold to Path
#os.environ['PATH'] = '$PATH;{}'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287/scripts/bin")
#os.environ['HOUDINI_PATH'] = '{};&'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287")

def main():
    subprocess.Popen(houdini)
    return 0

if __name__ == "__main__":
    sys.exit(main())
