#encoding=utf-8
import sys
sys.path.append('..')
import paramiko


class Ssh(object):
	
	#use paramiko to connect to the host,return conn
	def connect(self, host, username, password):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			ssh.connect(host,username=username,password=password,allow_agent=True,look_for_keys=True)
			return ssh
		except:
			return None

	def close(self, conn):
		try:
			conn.close
		except Exception as e:
			print(e)

	#use conn to execute the cmd and return the results of execute the cmd
	def exec_commands(self, conn, cmd):
		stdin,stdout,stderr = conn.exec_command(cmd)
		results=stdout.read()
		return results

	def ssh_scp_put(self, conn, local_file, remote_file):
		try:
			sftp = paramiko.SFTPClient.from_transport(conn.get_transport())
			sftp = conn.open_sftp()
			sftp.put(local_file, remote_file)
		except Exception as e:
			print(e)

	def ssh_scp_get(self, conn, remote_file, local_file):
		try:
			sftp = paramiko.SFTPClient.from_transport(conn.get_transport())
	 		sftp = conn.open_sftp()
	 		sftp.get(remote_file, local_file)
		except Exception as e:
			print(e)