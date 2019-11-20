cd /usr/local/mongodb
./mongod --config mongodb.conf   --auth


db.createUser({user:"admin",pwd:"123456",roles:["root"]})


db.createUser({user:"testAdmin",pwd:"123456",roles:[{role:"userAdminAnyDatabase",db:"admin"}]})


 --auth