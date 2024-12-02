import redis from 'redis';

const client = redis.createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.hset(hashName, fieldName, fieldValue, redis.print);
};

const printHash = (hashName) => {
  client.hgetall(hashName, (err, reply) => {
    console.log(reply);
  });
};

const mainHash = {
  hashObj: {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  },
  hash: () => {
    for (const [field, value] of Object.entries(mainHash.hashObj)) {
      updateHash('HolbertonSchools', field, value);
    }
    printHash('HolbertonSchools');
  },
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  mainHash.hash();
});
