const apiUrl = 'https://www.hastanemyanimda.com/api/users?branch_id=13';fetch(apiUrl)  .then(response => response.json())  .then(data => {    const users = data.map(user => ({      name: user.name,      imgUrl: `https://www.hastanemyanimda.com/${user.photo}`,      link: `https://www.hastanemyanimda.com/doktor/${user.slug}`    }));    // Diziyi kullanmak için burada yapmak istediğiniz işlemleri yazabilirsiniz    console.log(users);  })  .catch(error => console.error(error));