// use axios
// axios is Promise based HTTP client

import axios from 'axios';

export {};

let url: string = 
    'https://udemy-utils.herokuapp.com/api/v1/articles?token=token123';

// handle success
// only status code

// let data: any;
//let data: object[];

interface Article {
    id: number;
    title: string;
    description: string;
}
//let data: Article[];
let data: Article[];


axios.get(url)
    .then(function(response) {

    console.log(response.status);
    data = response.data;
    console.log(data);
    data = [
        {
            id: 1,
            title: 'title',
            description: 'description'
        }
    ];
    })
    .catch(function (error) {
        console.log(error)
    })
    .then(function () {
        // always executed
    });
/*
@mac ~/w/g/l/l/t/u/developer (typescript/20220609)> npm run dev src/any.ts 
Debugger attached.

> developer@1.0.0 dev
> ts-node-dev --respawn "src/any.ts"

Debugger attached.
[INFO] 10:45:55 ts-node-dev ver. 2.0.0 (using ts-node ver. 10.8.1, typescript ver. 4.7.3)
Debugger attached.
{
  status: 200,
  statusText: 'OK',
  headers: {
    server: 'Cowboy',
    date: 'Thu, 09 Jun 2022 01:45:58 GMT',
    connection: 'close',
    'x-frame-options': 'SAMEORIGIN',
    'x-xss-protection': '1; mode=block',
    'x-content-type-options': 'nosniff',
    'content-type': 'application/json; charset=utf-8',
    etag: 'W/"188ca0a37443fc2de47da0ee6bf8967b"',
    'cache-control': 'max-age=0, private, must-revalidate',
    'x-request-id': 'ba7f0974-48b8-48c8-928a-e73fe2266600',
    'x-runtime': '0.004521',
    vary: 'Origin',
    'transfer-encoding': 'chunked',
    via: '1.1 vegur'
  },
  config: {
    transitional: {
      silentJSONParsing: true,
      forcedJSONParsing: true,
      clarifyTimeoutError: false
    },
    adapter: [Function: httpAdapter],
    transformRequest: [ [Function: transformRequest] ],
    transformResponse: [ [Function: transformResponse] ],
    timeout: 0,
    xsrfCookieName: 'XSRF-TOKEN',
    xsrfHeaderName: 'X-XSRF-TOKEN',
    maxContentLength: -1,
    maxBodyLength: -1,
    env: { FormData: [Function] },
    validateStatus: [Function: validateStatus],
    headers: {
      Accept: 'application/json, text/plain, * /*',
      'User-Agent': 'axios/0.27.2'
    },
    method: 'get',
    url: 'https://udemy-utils.herokuapp.com/api/v1/articles?token=token123',
    data: undefined
  },
  request: <ref *1> ClientRequest {
    _events: [Object: null prototype] {
      abort: [Function (anonymous)],
      aborted: [Function (anonymous)],
      connect: [Function (anonymous)],
      error: [Function (anonymous)],
      socket: [Function (anonymous)],
      timeout: [Function (anonymous)],
      prefinish: [Function: requestOnPrefinish]
    },
    _eventsCount: 7,
    _maxListeners: undefined,
    outputData: [],
    outputSize: 0,
    writable: true,
    destroyed: false,
    _last: true,
    chunkedEncoding: false,
    shouldKeepAlive: false,
    maxRequestsOnConnectionReached: false,
    _defaultKeepAlive: true,
    useChunkedEncodingByDefault: false,
    sendDate: false,
    _removedConnection: false,
    _removedContLen: false,
    _removedTE: false,
    _contentLength: 0,
    _hasBody: true,
    _trailer: '',
    finished: true,
    _headerSent: true,
    _closed: false,
    socket: TLSSocket {
      _tlsOptions: [Object],
      _secureEstablished: true,
      _securePending: false,
      _newSessionPending: false,
      _controlReleased: true,
      secureConnecting: false,
      _SNICallback: null,
      servername: 'udemy-utils.herokuapp.com',
      alpnProtocol: false,
      authorized: true,
      authorizationError: null,
      encrypted: true,
      _events: [Object: null prototype],
      _eventsCount: 10,
      connecting: false,
      _hadError: false,
      _parent: null,
      _host: 'udemy-utils.herokuapp.com',
      _readableState: [ReadableState],
      _maxListeners: undefined,
      _writableState: [WritableState],
      allowHalfOpen: false,
      _sockname: null,
      _pendingData: null,
      _pendingEncoding: '',
      server: undefined,
      _server: null,
      ssl: [TLSWrap],
      _requestCert: true,
      _rejectUnauthorized: true,
      parser: null,
      _httpMessage: [Circular *1],
      [Symbol(res)]: [TLSWrap],
      [Symbol(verified)]: true,
      [Symbol(pendingSession)]: null,
      [Symbol(async_id_symbol)]: 12,
      [Symbol(kHandle)]: [TLSWrap],
      [Symbol(lastWriteQueueSize)]: 0,
      [Symbol(timeout)]: null,
      [Symbol(kBuffer)]: null,
      [Symbol(kBufferCb)]: null,
      [Symbol(kBufferGen)]: null,
      [Symbol(kCapture)]: false,
      [Symbol(kSetNoDelay)]: false,
      [Symbol(kSetKeepAlive)]: true,
      [Symbol(kSetKeepAliveInitialDelay)]: 60,
      [Symbol(kBytesRead)]: 0,
      [Symbol(kBytesWritten)]: 0,
      [Symbol(connect-options)]: [Object],
      [Symbol(RequestTimeout)]: undefined
    },
    _header: 'GET /api/v1/articles?token=token123 HTTP/1.1\r\n' +
      'Accept: application/json, text/plain, * /*\r\n' +
      'User-Agent: axios/0.27.2\r\n' +
      'Host: udemy-utils.herokuapp.com\r\n' +
      'Connection: close\r\n' +
      '\r\n',
    _keepAliveTimeout: 0,
    _onPendingData: [Function: nop],
    agent: Agent {
      _events: [Object: null prototype],
      _eventsCount: 2,
      _maxListeners: undefined,
      defaultPort: 443,
      protocol: 'https:',
      options: [Object: null prototype],
      requests: [Object: null prototype] {},
      sockets: [Object: null prototype],
      freeSockets: [Object: null prototype] {},
      keepAliveMsecs: 1000,
      keepAlive: false,
      maxSockets: Infinity,
      maxFreeSockets: 256,
      scheduling: 'lifo',
      maxTotalSockets: Infinity,
      totalSocketCount: 1,
      maxCachedSessions: 100,
      _sessionCache: [Object],
      [Symbol(kCapture)]: false
    },
    socketPath: undefined,
    method: 'GET',
    maxHeaderSize: undefined,
    insecureHTTPParser: undefined,
    path: '/api/v1/articles?token=token123',
    _ended: true,
    res: IncomingMessage {
      _readableState: [ReadableState],
      _events: [Object: null prototype],
      _eventsCount: 4,
      _maxListeners: undefined,
      socket: [TLSSocket],
      httpVersionMajor: 1,
      httpVersionMinor: 1,
      httpVersion: '1.1',
      complete: true,
      rawHeaders: [Array],
      rawTrailers: [],
      aborted: false,
      upgrade: false,
      url: '',
      method: null,
      statusCode: 200,
      statusMessage: 'OK',
      client: [TLSSocket],
      _consuming: true,
      _dumped: false,
      req: [Circular *1],
      responseUrl: 'https://udemy-utils.herokuapp.com/api/v1/articles?token=token123',
      redirects: [],
      [Symbol(kCapture)]: false,
      [Symbol(kHeaders)]: [Object],
      [Symbol(kHeadersCount)]: 28,
      [Symbol(kTrailers)]: null,
      [Symbol(kTrailersCount)]: 0,
      [Symbol(RequestTimeout)]: undefined
    },
    aborted: false,
    timeoutCb: null,
    upgradeOrConnect: false,
    parser: null,
    maxHeadersCount: null,
    reusedSocket: false,
    host: 'udemy-utils.herokuapp.com',
    protocol: 'https:',
    _redirectable: Writable {
      _writableState: [WritableState],
      _events: [Object: null prototype],
      _eventsCount: 3,
      _maxListeners: undefined,
      _options: [Object],
      _ended: true,
      _ending: true,
      _redirectCount: 0,
      _redirects: [],
      _requestBodyLength: 0,
      _requestBodyBuffers: [],
      _onNativeResponse: [Function (anonymous)],
      _currentRequest: [Circular *1],
      _currentUrl: 'https://udemy-utils.herokuapp.com/api/v1/articles?token=token123',
      [Symbol(kCapture)]: false
    },
    [Symbol(kCapture)]: false,
    [Symbol(kNeedDrain)]: false,
    [Symbol(corked)]: 0,
    [Symbol(kOutHeaders)]: [Object: null prototype] {
      accept: [Array],
      'user-agent': [Array],
      host: [Array]
    }
  },
  data: [
    {
      id: 1,
      title: 'Title for article #1!',
      description: 'Description for article #1.'
    },
    {
      id: 2,
      title: 'Title for article #2!',
      description: 'Description for article #2.'
    },
    {
      id: 3,
      title: 'Title for article #3!',
      description: 'Description for article #3.'
    },
    {
      id: 4,
      title: 'Title for article #4!',
      description: 'Description for article #4.'
    },
    {
      id: 5,
      title: 'Title for article #5!',
      description: 'Description for article #5.'
    },
    {
      id: 6,
      title: 'Title for article #6!',
      description: 'Description for article #6.'
    },
    {
      id: 7,
      title: 'Title for article #7!',
      description: 'Description for article #7.'
    },
    {
      id: 8,
      title: 'Title for article #8!',
      description: 'Description for article #8.'
    },
    {
      id: 9,
      title: 'Title for article #9!',
      description: 'Description for article #9.'
    },
    {
      id: 10,
      title: 'Title for article #10!',
      description: 'Description for article #10.'
    }
  ]
}
Waiting for the debugger to disconnect...
*/