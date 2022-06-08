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

# Install ts-node
1. `npm install ts-node@latest`
2. `ts-node -v`
   
# Build and run
1. `ts-node src/install-typescript.ts`
   1. `{ message: 'Hello tyepscript' }`
2. `npx ts-node src/install-typescript.ts `

# ts-node-dev
1. Automatic detection and run
   1. Install
      1. `npm install --save-dev ts-node-dev@latest`
   2. set
      1. ` npx ts-node-dev --respawn src/install-typescript.ts `
         1. `{ message: 'Hello ts-node' }`
         2. option
            1. --respawn
               1. `auto detection`
            2. --transpileOnly
               1. `not complie`
   3. Modify and save of src/install-typescript.ts
      1. `[INFO] 10:31:27 Restarting: /xxxx/developer/src/install-typescript.ts has been modified`
         `{ message: 'Hello ts-node-dev' }` 

# Set ts-node-dev

## Set ts-node-dev -on package.json
```typescript
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "ts-node-dev --respawn"
  },
```
## Execute npm run
```shell
xxx@mac ~/w/g/l/l/t/u/developer (typescript/20220608) [SIGINT]> npm run dev src/install-typescript.ts
Debugger attached.

> developer@1.0.0 dev
> ts-node-dev --respawn "src/install-typescript.ts"

Debugger attached.
[INFO] 10:44:15 ts-node-dev ver. 2.0.0 (using ts-node ver. 10.8.1, typescript ver. 4.7.3)
Debugger attached.
{ message: 'Hello ts-node-dev' }
Waiting for the debugger to disconnect...
```

# tsconfig.json
## Create
`npx tsc --init`
