export {};

function error(message: string): never {
  throw new Error(message);
}


try {
  let result = error('test');
  console.log({result});
} catch(error) {
  console.log( { error });
}

let foo: void = undefined;
//let bar: never = undefined
let bar: never = error('only me!');

/* 
[INFO] 14:36:31 ts-node-dev ver. 2.0.0 (using ts-node ver. 10.8.1, typescript ver. 4.7.3)
{
  error: Error: test
      at error (/Users/xxx/work/git/learn/language/typescript/udemy/developer/src/file:/Users/xxx/work/git/learn/language/typescript/udemy/developer/src/never.ts:4:9)
      at Object.<anonymous> (/Users/xx/work/git/learn/language/typescript/udemy/developer/src/file:/Users/xxx/work/git/learn/language/typescript/udemy/developer/src/never.ts:9:16)
      at Module._compile (node:internal/modules/cjs/loader:1099:14)
      at Module._compile (/Users/xxx/work/git/learn/language/typescript/udemy/developer/node_modules/source-map-support/source-map-support.js:568:25)
      at Module.m._compile (/private/var/folders/cm/ty1ntb494s5b10bm8f7421kr0000gn/T/ts-node-dev-hook-3968552924094477.js:69:33)
      at Module._extensions..js (node:internal/modules/cjs/loader:1153:10)
      at require.extensions..jsx.require.extensions..js (/private/var/folders/cm/ty1ntb494s5b10bm8f7421kr0000gn/T/ts-node-dev-hook-3968552924094477.js:114:20)
      at require.extensions.<computed> (/private/var/folders/cm/ty1ntb494s5b10bm8f7421kr0000gn/T/ts-node-dev-hook-3968552924094477.js:71:20)
      at Object.nodeDevHook [as .ts] (/Users/xxx/work/git/learn/language/typescript/udemy/developer/node_modules/ts-node-dev/lib/hook.js:63:13)
      at Module.load (node:internal/modules/cjs/loader:975:32)
}

*/


/*
[ERROR] 14:42:40 Error: only me!
*/