
import subprocess, sys, os;

def configure_devops_system(sequence_of_configuration_dict):
    for configuration_dict in sequence_of_configuration_dict:
        print(configuration_dict['note']);
        if os.system(configuration_dict['config_command']) != 0:
            print(configuration_dict['failed_note']);
            sys.exit();

def main():
    sequence_of_configuration_dict = ({'note':'\n[+] update the package lists\n', 'config_command':'sudo apt update', 'failed_note':'\n[-] unable to update the package\n'},
                                      {'note':'\n[+] install package installer for python\n', 'config_command':'sudo apt install -y python3-pip', 'failed_note':'\n[-] python3-pip installation is failed\n'},
                                      {'note':'\n[+] install netmiko library\n', 'config_command':'pip install netmiko', 'failed_note':'\n[-] unable to install netmiko library\n'},
                                      {'note':'\n[+] install napalm library\n', 'config_command':'pip install napalm', 'failed_note':'\n[-] unable to install napalm library\n'},
                                      {'note':'\n[+] install apache2\n', 'config_command':'sudo apt install -y apache2', 'failed_note':'\n[-] apache2 installation is failed\n'},
                                      {'note':'\n[+] disable apache2\'s mpm_event module\n', 'config_command':'sudo a2dismod mpm_event', 'failed_note':'\n[-] unable to disable the module\n'},
                                      {'note':'\n[+] enable apache2\'s mpm_prefork and cgi module\n', 'config_command':'sudo a2enmod mpm_prefork cgi', 'failed_note':'\n[-] unable to enable the module\n'},
                                      {'note':'\n[+] reconfigure apache2\'s configuration', 'config_command':'sudo cp tmp/000-default.conf /etc/apache2/sites-enabled/000-default.conf', 'failed_note':'\n[-] unable to reconfigure apache2\'s configuration\n'},
                                      {'note':'\n[+] restart apache2\'s service\n', 'config_command':'sudo service apache2 restart', 'failed_note':'\n[-] unable to restart apache2\'s service\n'});
    configure_devops_system(sequence_of_configuration_dict);

if __name__=='__main__':
    if os.getuid() != 0:
        print('\n... require administrative privilege to run the program\n');
        sys.exit();
    else:
        main();
        