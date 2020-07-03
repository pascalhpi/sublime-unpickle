import subprocess

import sublime
import sublime_plugin


class UnpickleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # use systems python3 pickle, because it is probably the same that created the pickle files
        try:
            unpickled = '<br>unpickled content:<br><br>' + subprocess.check_output(
                ['python3', '-m', 'pickle', self.view.file_name()], universal_newlines=True)
        except:
            unpickled = '<br>Error: Not a pickle file!'

        self.view.erase_phantoms('unpickle')
        # 10**10 is just a hack to get to the bottom. What's the proper way to do this?
        self.view.add_phantom('unpickle', sublime.Region(10**10, 10**10+1),
                              unpickled, sublime.LAYOUT_BLOCK)
        self.view.show(10**10)
