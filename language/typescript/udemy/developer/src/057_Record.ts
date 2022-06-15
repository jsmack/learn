export {};


// recoard take two argments
// Recoard<K, T>


type Prefectures = 'Tokyo' | 'Chiba' | 'Kanagawa' | 'Saitama';

type Covid19InfectionInfo = {
    name: string;
    confirmed_cases: number;
};


// const covid19Japan = {
//     Tokyo: { name: '東京', conffirmed_cases: 1900},
//     Chiba: { name: '千葉', conffirmed_cases: 1930},
//     Kanagawa: { name: '神奈川', conffirmed_cases: 1940},
//     Saitama: { name: '埼玉', conffirmed_cases: 2}
// }

const covid19Japan: Record<Prefectures, Covid19InfectionInfo> = {
    Tokyo: { name: '東京', confirmed_cases: 1900},
    Chiba: { name: '千葉', confirmed_cases: 1930},
    Kanagawa: { name: '神奈川', confirmed_cases: 1940},
    Saitama: { name: '埼玉', confirmed_cases: 13}
}
