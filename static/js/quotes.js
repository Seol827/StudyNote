const quotes = [
    {
        quote : "때론 기회를 놓치는 것이 기회일 수 있다.",
        author : ".·:*¨༺ 벤자민 버튼의 시간은 거꾸로 간다 中 ༻¨*:·.",
    },
    {
        quote : "영원히 살 것처럼 꿈꾸고 오늘 죽을 것처럼 살아라",
        author : ".·:*¨༺ 제임스틴 ༻¨*:·.",
    },
    {
        quote : "우리가 꿈꿀 수 있다면, 이룰 수도 있습니다.",
        author : ".·:*¨༺ 월트 디즈니 ༻¨*:·.",
    },
    {
        quote : "인생에서 원하는 것을 얻기 위한 첫번째 단계는 내가 무엇을 원하는지 결정하는 것이다.",
        author : ".·:*¨༺ 벤 스타인 ༻¨*:·.",
    },
    {
        quote : "긴 인생은 충분히 좋지 않을 수 있다. 그러나 좋은 인생은 충분히 길다.",
        author : ".·:*¨༺ 벤자민 프랭클린 ༻¨*:·.",
    },
    {
        quote : "인생은 자전거를 타는 것과 같다. 계속 페달을 밟는 한 넘어질 염려는 없다.",
        author : ".·:*¨༺ 클라우드 페퍼 ༻¨*:·.",
    },
    {
        quote : "서두르지 말되 멈추지 말라",
        author : ".·:*¨༺ 괴테 ༻¨*:·.",
    },
    {
        quote : "생각하고 살지 않으면, 사는 대로 생각하게 된다.",
        author : ".·:*¨༺ 폴 발레리 ༻¨*:·.",
    },
    {
        quote : "과거에서 교훈을 얻을 수는 있어도 과거 속에서 살 수는 없다.",
        author : ".·:*¨༺ 린든 B.존슨 ༻¨*:·.",
    },
    {
        quote : "삶의 의미는 발견하는 것이 아니라 만들어가는 것이다.",
        author : ".·:*¨༺ 생텍쥐페리 ༻¨*:·.",
    }
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;