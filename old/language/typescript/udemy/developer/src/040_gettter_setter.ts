
export {};

// * owner
//  * 所有者
//  * 初期化時に設定可能
//  * 途中で変更不可
//  * 参照可能
// * secretNumber
//  * 個人番号
//  * 初期化時に設定可能
//  * 途中で変更
//  * 参照不可

class MyNumberCard {
    private _owner: string;
    private _secretNumber: number;

    constructor (owner: string, secretNumber: number) {
        this._owner = owner;
        this._secretNumber = secretNumber;
    }
    // fix complioption to tsconfig.json
    get owner(): string {
        return this._owner;
    }
    set secretNumber(secretNumber: number) {
        this._secretNumber = secretNumber;
    }

    debugPrint() {
        return `secretNumber: ${this._secretNumber}`;
    }
}


const card = new MyNumberCard('Ham', 1234567890);
console.log(card.owner);
// src/040_gettter_setter.ts(35,6): error TS2540: Cannot assign to 'owner' because it is a read-only property.
// card.owner = 'Tom';

console.log(card.debugPrint());
//secretNumber: 1234567890

card.secretNumber = 987654321;
console.log(card.debugPrint());
//secretNumber: 987654321