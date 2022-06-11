
export {};

// シグネチャ：こういう関数を使うという宣言
// ここで型チェックが可能となる
function double(value: number): number;
function double(value: string): string;

// union(string | number)で行わず、ここでは型制約をしない(stringとかを指定しない)
function double(value: any): any {
    console.log(typeof value);
    if (typeof value === 'string') { 
        return value + value;
// Auto check by Signature
//    } else if ( typeof value == 'number') {
//        return value * 2;
//    } else {
//        throw 'number nor string. check argument type';
//    }
    } else {
        return value * 2;
    }
}

//function double(value: string): string {
//    return value + value;
//}

console.log(double(100));
// 200
console.log(double('Type '));
// Type Type
//console.log(double(false));
