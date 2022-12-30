
export {};

// readonly propertiy
class VisaCard {
    //readonly owner: string;

    //constructor (owner: string) {
    //    this.owner = owner;
    //}
    constructor (public readonly owner: string) {

    }
}

const myVisaCard = new VisaCard('Tom');
console.log(myVisaCard);

//Cannot assign to 'owner' because it is a read-only property.ts(2540)
//myVisaCard.owner = 'Hanks';