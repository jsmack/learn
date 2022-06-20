import { nodeModuleNameResolver } from "typescript";

export {};

type DebugType = () => void;
//type DebugType = () => void


type SomeTypes = string | number | DebugType;
//type SomeTypes = string | number | DebugType


type FunctionType = Exclude<SomeTypes, number|string>;
//type FunctionType = () => void




type FunctionTypeByExctract = Extract<SomeTypes, DebugType>;
//type FunctionTypeByExctract = () => void



type NullableTypes = string | number | undefined;
//type NullableTypes = string | number | undefined


type NonNullableTypes = NonNullable<NullableTypes>;
//type NonNullableTypes = string | number



type MyExclude<T, U> = T extends U ? never : T;
type MyFunctionType = MyExclude<SomeTypes, string | number>;
//type MyFunctionType = () => void


type MyExclude2<T> = T extends string | number ? never : T;
type MyFunctionType2 = MyExclude2<SomeTypes>;

type MyExclude3 = 
    | (string extends string | number ? never : string)       //never
    | (number extends string | number ? never : number)       //never
    | (DebugType extends string | number ? never : DebugType) //Debugtype
