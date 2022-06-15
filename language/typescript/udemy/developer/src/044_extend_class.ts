export {};

class Animal {
    constructor(public name: string) {}
    run(): string {
        return 'Run';
    }
}

class Lion extends Animal {
    public speed: number;

    constructor(name: string, speed: number) {
        super(name);
        this.speed = speed;
    }
    run (): string {
        //const parentMessage = super.run();
        return `${super.run()} ${this.speed}km`;
    }
}


let animal = new Animal('Dog');
console.log(animal.run());

let lion = new Lion('Tiger',500);
console.log(lion.run());
console.log(lion);
//Lion { name: 'Simba', speed: 200 }

console.log(new Lion('Simba',200).run());
//Run 200km