export {};


class Me { 
    static isProgrammer: boolean = true;
    static firstName: string = 'Tom';
    static lastName: string = 'Hanks';
    
    static work (): string {
        return `Hey!Hey!Hey! ${this.firstName}`; 
    }
}


//let me = new Me();
//console.log(me.isProgrammer);
//me.isProgrammer = false;
//console.log(me.isProgrammer);


console.log(Me.isProgrammer);
console.log(Me.work());