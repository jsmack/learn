export {};

//let profile = ['Tom', 43];
// declare tuple
let profile: [string, number] = ['Tom', 43];

// compile error type unmatch
profile = [43, 'Tom'];
