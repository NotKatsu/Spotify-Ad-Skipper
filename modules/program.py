import psutil

from typing import Union

class Program:
    def is_running(task_name: str) -> bool:
        """Check if a program is running and return True/False.

        Args:
            task_name (str): The name the program should be running as.

        Returns:
            bool: If program is running or not
        """
        
        if task_name.endswith(".exe"):
            for program in psutil.process_iter():
                if program.name() == task_name:
                    return True
                
            return False
                
        else:
            for program in psutil.process_iter():
                if program.name() == f"{task_name}.exe":
                    return True
                
            return False
        
    def information(task_name: str) -> Union[None, object]:
        """Get information about a process.

        Args:
            task_name (str): The name of the process you want the information on.

        Returns:
            Union[None, object]: Return None if process not found else an object.
        """
        
        if task_name.endswith(".exe"):
            for program in psutil.process_iter():
                if program.name() == task_name:
                    return program
                
            return None
                
        else:
            for program in psutil.process_iter():
                if program.name() == f"{task_name}.exe":
                    return program
                
            return None
        
    def kill(task_name: str) -> bool:
        try:
            if task_name.endswith(".exe"):
                for program in psutil.process_iter():
                    if program.name() == task_name:
                        program.terminate(); return True
                    
                return False
                    
            else:
                for program in psutil.process_iter():
                    if program.name() == f"{task_name}.exe":
                        program.terminate(); return True 
        except:
            return False