let instaObjects;
let twitchObjects;

let instaDateList = [];
let twitchDateList = [];

let instCountList = [];
let twitchCountList = [];

let months = {
  "01": "Января",
  "02": "Февраля",
  "03": "Марта",
  "04": "Апреля",
  "05": "Мая",
  "06": "Июня",
  "07": "Июля",
  "08": "Августа",
  "09": "Сентября",
  "10": "Октября",
  "11": "Ноября",
  "12": "Декабря"
};

let addObjectValueToList = (objectsArr, datesArr, key) => {
  objectsArr.forEach(element => {
    if (key == "created_dt") {
      let tempList = element[key].split("-");
      console.log(tempList);
      let temp = `${tempList[2]}\t${months[tempList[1]]}`;
      console.log(temp);
      datesArr.push(temp);
    } else {
      datesArr.push(element[key]);
    }
  });
};

let url = "http://maddynyan.ru/api/statistics";
fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    instaObjects = data["insta"];
    twitchObjects = data["twitch"];
    addObjectValueToList(instaObjects, instaDateList, "created_dt");
    addObjectValueToList(twitchObjects, twitchDateList, "created_dt");
    addObjectValueToList(instaObjects, instCountList, "count");
    addObjectValueToList(twitchObjects, twitchCountList, "count");
  })
  .then(() => {
    console.log(twitchCountList);
    var ctx = document.getElementById("myChart").getContext("2d");
    var myLineChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: instaDateList,
        datasets: [
          {
            label: "Инстаграм",
            borderColor: "rgb(255, 99, 132)",
            borderWidth: 7,
            fill: false,
            data: [
              { x: 0, y: instCountList[0] },
              { x: 1, y: instCountList[1] },
              { x: 2, y: instCountList[2] },
              { x: 3, y: instCountList[3] },
              { x: 4, y: instCountList[4] },
              { x: 5, y: instCountList[5] },
              { x: 6, y: instCountList[6] }
            ]
          },
          {
            label: "Твич",
            borderColor: "rgb(31, 10, 132)",
            borderWidth: 7,
            fill: false,
            data: [
              { x: 0, y: twitchCountList[0] },
              { x: 1, y: twitchCountList[1] },
              { x: 2, y: twitchCountList[2] },
              { x: 3, y: twitchCountList[3] },
              { x: 4, y: twitchCountList[4] },
              { x: 5, y: twitchCountList[5] },
              { x: 6, y: twitchCountList[6] }
            ]
          }
        ]
      },
      options: {}
    });
  })
  .catch(err => {
    alert('Ошибка, мда')
  });

