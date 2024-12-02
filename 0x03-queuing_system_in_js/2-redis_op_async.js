import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.get).bind(client)(schoolName));
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
