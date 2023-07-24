'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    return queryInterface.bulkInsert('users', [{
      username: 'hardiantojp',
      email: 'ekskulkom.ardhi@gmail.com',
      password: '$2y$10$0eGzoVssGKBYOXSpcsX.IutiWAVPoyT9.utNXLrIC1wBxxr7d2Cxa',
      name: 'John Doe',
      status: 'active'
    }]);
  },

  async down (queryInterface, Sequelize) {
    return queryInterface.bulkDelete('users', null, {});
  }
};
