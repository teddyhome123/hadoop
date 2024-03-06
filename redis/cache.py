import subprocess
import redis

redis_host = 'localhost'
redis_port = 6379
redis_db = 0

hadoop_output_file = '/tmp/hadoop-yarn/staging/history/done_intermediate/hadoop/job_1709142061549_0003.summary'

r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

def get_hadoop_output(hadoop_output_path):
    cat_process = subprocess.Popen(['docker', 'exec', 'repo_namenode_1', 'hadoop', 'fs', '-cat', hadoop_output_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cat_process.communicate()
    if error:
        print(f"Error retrieving Hadoop job output: {error}")
        return None
    return output.decode('iso-8859-1')

def write_to_redis(key, value):
    try:
        r.set(key, value)
        print(f"Data written to Redis under key: {key}")
    except Exception as e:
        print(f"Failed to write to Redis: {e}")

output = get_hadoop_output(hadoop_output_file)
if output is not None:
    redis_key = "hadoop:job_1709142061549_0003:summary"
    write_to_redis(redis_key, output)

