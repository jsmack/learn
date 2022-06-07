# Setup
1. create package.json
   1. `npm init -y`
2. Install type scrit
   1. set repository
      1. ` npm config set registry http://registry.npmjs.org`
   2. Show latest version
      1. `npm info typescrpt`
   3. Install
      1. `npm install --save-dev typescript@4.7.3`
         1. `--save-dev` is local install
         2. `--global` is global install

# Build
1. Create source　file
2. Compile or
   1. `tsc src/install-typescript.ts`
   2. `npx tsc src/install-typescript.ts`
3. check
   1. That the js file was created in the same directory as the ts file location.

# Run
1. `node src/install-typescript.js `
   1. `{ message: 'Hello tyepscript' }`