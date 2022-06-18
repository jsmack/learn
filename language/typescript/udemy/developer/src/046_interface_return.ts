export {};


class Magic {}
class Souryo {}

class Taro extends Magic {}

interface Kenja {
    iona(): void;
}
interface Warrior {
    attack(): void;
}

// need from implements declare method
// implementsは宣言を強制させるため、忘れ防止にできる。
class Jiro implements Kenja, Warrior{
    iona(): void {
        console.log('iona');
    }
    attack(): void {
        console.log('attack');
    }
}

const jiro = new Jiro();
jiro.attack();
jiro.iona();
console.log('test');