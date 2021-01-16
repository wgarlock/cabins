import http from 'k6/http';
import { sleep } from 'k6';

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
        http_req_duration: ['p(95)<500'],
        http_req_duration: ['max<2000'],
    }
};

export default function () {
  let res = http.get('https://cabins.dev');
  sleep(1);
}
