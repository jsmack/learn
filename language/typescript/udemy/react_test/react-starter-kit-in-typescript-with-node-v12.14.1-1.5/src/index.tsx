import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
//htmlを表示するための部品

//ReactDOM.render(<App />, document.getElementById('root'));
//レンダーメソッド
//jsxで表現されているデータ
// rootは  public/index.htmlのdivタグにid="root"がありそこと紐づいている
// Appの場所は ./AppでありAppコンポーネントの場所は 同一ディレクトリの App.tsx

//type Foo = JSX.IntrinsicAttributes;


// index.tsxからapp.tsxにデータを渡す
// App.tsxにpropsを追加したらエラー消えた
ReactDOM.render(
// nameはApp.tsxにて許可しないようにしたのでエラーとなる
//    <App message="Nyan meow"  name="Cat Cat Cat" />, 
    <App message="Nyan meow"   />, 
    document.getElementById('root')
);


