'''Download audio and/or video from youtube'''

import sys
from workflow import Workflow

def main(wf):
    '''Main function. This is where the magic happens'''
    options = ['Audio', 'Video', 'Both']

    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for option in options:
        wf.add_item(title=option,
                    arg=option,
                    valid=True)

    # Send the results to Alfred as XML
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
