import { nodeModuleNameResolver } from "typescript";

export {};

type DebugType = () => void;
//type DebugType = () => void


type SomeTypes = string | number | DebugType;
//type SomeTypes = string | number | DebugType


type FunctionType = Exclude<SomeTypes, number|string>;
//type FunctionType = () => void


type NonFunctionType = Exclude<SomeTypes, DebugType>;
//type NonFunctionType = string | number


type TypeExcludingFunction = Exclude<SomeTypes, Function>;
//type TypeExcludingFunction = string | number


type FunctionTypeByExctract = Extract<SomeTypes, DebugType>;
//type FunctionTypeByExctract = () => void


type NonfunctionTypeByExtract = Extract<SomeTypes, string| number>;
//type NonfunctionTypeByExtract = string | number


type FunctionTypeExtractingFunction = Extract<SomeTypes, Function>;
//type FunctionTypeExtractingFunction = () => void


type NullableTypes = string | number | undefined;
//type NullableTypes = string | number | undefined


type NonNullableTypes = NonNullable<NullableTypes>;
//type NonNullableTypes = string | number

