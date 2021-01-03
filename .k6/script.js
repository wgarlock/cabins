import http from 'k6/http';
import { sleep } from 'k6';
import { Gauge } from 'k6/metrics';

let myPerformData = new Gauge('perform_data');


export let options = {
    stages: [
        { duration: '30s', target: 10 },
        { duration: '30s', target: 10 },
        { duration: '30s', target: 0 },
        { duration: '30s', target: 0 },
        { duration: '30s', target: 15 },
        { duration: '30s', target: 15 },
        { duration: '30s', target: 0 },
        { duration: '30s', target: 0 },
        { duration: '30s', target: 20 },
        { duration: '30s', target: 20 },
        { duration: '30s', target: 0 },

      ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95 percent of response times must be below 500ms
        http_req_duration: ['max<2000'], // 95 percent of response times must be below 500ms
    }
};

class TimeSeries {
    constructor(){
        this.time = []
        this.obj = []
    }

    add (time, obj){
        this.time.push(time)
        this.obj.push(obj)
    }
}

let dataSeries = new TimeSeries()

export default function () {
  let res = http.get('https://cabins.dev');
  sleep(1);
}
