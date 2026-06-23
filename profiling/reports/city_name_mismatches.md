# City Name Mismatch Report

Generated: 2026-06-23

---

## Summary

| Metric | Value |
|---|---|
| IBGE municipalities | 5571 |
| IBGE districts | 10751 |
| Distinct (city, state) pairs in our data | 8616 |
|  |  |
| 1. Matched at município level | 7476 |
| 2. Matched at distrito level | 763 |
| 3. Fuzzy suggestion available | 168 |
| 4. Matched via ViaCEP | 147 |
| 5. No confident match | 62 |
|  |  |
| IBGE exact match rate (tiers 1 + 2) | 95.6% |
| Overall resolution rate (tiers 1 + 2 + 4) | 97.3% |

Fuzzy threshold: 0.85 (SequenceMatcher ratio, same-state candidates only).
ViaCEP CEP format: 5-digit zip prefix + '000'.

---

## Section 1 — Matched at município level

7476 pairs matched exactly against the IBGE município list after normalisation.
No action required for these.

---

## Section 2 — Matched at distrito level

763 pairs matched the IBGE distrito list but not the município list.
These are valid Brazilian administrative units at district granularity.

| Raw city | State | Sources | Affected rows |
|---|---|---|---|
| `bonfim paulista` | SP | customers, geolocation | 144 |
| `barra de sao joao` | RJ | customers, geolocation | 101 |
| `arraial d'ajuda` | BA | customers, geolocation | 79 |
| `cachoeira do campo` | MG | customers, geolocation | 70 |
| `abrantes` | BA | customers, geolocation | 47 |
| `jacare` | SP | customers, geolocation | 43 |
| `posto da mata` | BA | customers, geolocation | 42 |
| `governador portela` | RJ | customers, geolocation | 39 |
| `monte verde` | MG | customers, geolocation | 39 |
| `trancoso` | BA | customers, geolocation | 38 |
| `itaipava` | ES | customers, geolocation | 35 |
| `avelar` | RJ | customers, geolocation | 33 |
| `sao vicente de paula` | RJ | geolocation | 27 |
| `azurita` | MG | customers, geolocation | 23 |
| `perpetuo socorro` | MG | customers, geolocation | 23 |
| `santo amaro de campos` | RJ | customers, geolocation | 20 |
| `bacaxa` | RJ | customers, geolocation | 19 |
| `nossa senhora do o` | PE | customers, geolocation | 18 |
| `maresias` | SP | geolocation | 18 |
| `antonio pereira` | MG | customers, geolocation | 17 |
| `itabata` | BA | geolocation | 17 |
| `jamapara` | RJ | customers, geolocation | 16 |
| `barra de são joão` | RJ | geolocation | 16 |
| `conservatoria` | RJ | customers, geolocation | 15 |
| `ibitiuva` | SP | customers, geolocation | 15 |
| `santo antonio dos campos` | MG | customers, geolocation | 15 |
| `alexandrita` | MG | customers, geolocation | 13 |
| `alto alegre` | PR | customers, geolocation | 13 |
| `california da barra` | RJ | customers, geolocation | 13 |
| `lidice` | RJ | customers, geolocation | 13 |
| `luizlandia do oeste` | MG | customers, geolocation | 13 |
| `monte gordo` | BA | customers, geolocation | 13 |
| `sao jose do turvo` | RJ | customers, geolocation | 13 |
| `arrozal` | RJ | customers, geolocation | 12 |
| `barao de juparana` | RJ | customers, geolocation | 12 |
| `werneck` | RJ | customers, geolocation | 12 |
| `amarantina` | MG | geolocation | 12 |
| `ibitira` | MG | geolocation | 12 |
| `igarai` | SP | geolocation | 12 |
| `sao francisco xavier` | SP | geolocation | 12 |
| `murucupi` | PA | customers, geolocation | 11 |
| `praia grande` | ES | customers, geolocation | 11 |
| `vila nova` | PR | customers, geolocation | 11 |
| `aparecida de sao manuel` | SP | customers, geolocation | 10 |
| `arace` | ES | customers, geolocation | 10 |
| `extrema` | RO | customers, geolocation | 10 |
| `maristela` | SP | customers, geolocation | 10 |
| `santanesia` | RJ | customers, geolocation | 10 |
| `sao joao do paraiso` | RJ | customers, geolocation | 10 |
| `vargem alegre` | RJ | customers, geolocation | 10 |
| `senhora das dores` | MG | geolocation | 10 |
| `itacurussa` | RJ | customers, geolocation | 9 |
| `passa tres` | RJ | customers, geolocation | 9 |
| `pirapo` | PR | customers, geolocation | 9 |
| `portela` | RJ | customers, geolocation | 9 |
| `pureza` | RJ | customers, geolocation | 9 |
| `quatituba` | MG | customers, geolocation | 9 |
| `raposo` | RJ | customers, geolocation | 9 |
| `rechan` | SP | customers, geolocation | 9 |
| `vila pereira` | MG | customers, geolocation | 9 |
| `passagem de mariana` | MG | geolocation | 9 |
| `anta` | RJ | customers, geolocation | 8 |
| `areia branca dos assis` | PR | customers, geolocation | 8 |
| `braco do rio` | ES | customers, geolocation | 8 |
| `cachoeira do brumado` | MG | customers, geolocation | 8 |
| `celina` | ES | customers, geolocation | 8 |
| `cocais` | MG | customers, geolocation | 8 |
| `espigao` | SP | customers, geolocation | 8 |
| `glicerio` | RJ | customers, geolocation | 8 |
| `itaoca` | ES | customers, geolocation | 8 |
| `morro do ferro` | MG | customers, geolocation | 8 |
| `novo brasil` | ES | customers, geolocation | 8 |
| `andrade pinto` | RJ | geolocation | 8 |
| `corrego do ouro` | MG | geolocation | 8 |
| `correia de almeida` | MG | geolocation | 8 |
| `dorandia` | RJ | geolocation | 8 |
| `sao pedro do avai` | MG | geolocation | 8 |
| `sao sebastiao do sacramento` | MG | geolocation | 8 |
| `taboas` | RJ | geolocation | 8 |
| `ibiraja` | BA | customers, geolocation | 7 |
| `irape` | SP | customers, geolocation | 7 |
| `itamira` | BA | customers, geolocation | 7 |
| `macuco de minas` | MG | customers, geolocation | 7 |
| `tapinas` | SP | customers, geolocation | 7 |
| `barcelos` | RJ | geolocation | 7 |
| `comendador venancio` | RJ | geolocation | 7 |
| `guarda dos ferreiros` | MG | geolocation | 7 |
| `jaci parana` | RO | geolocation | 7 |
| `jordanesia` | SP | geolocation | 7 |
| `lagoa bonita` | MS | geolocation | 7 |
| `merces de agua limpa` | MG | geolocation | 7 |
| `novo sarandi` | PR | geolocation | 7 |
| `quintao` | RS | geolocation | 7 |
| `realeza` | MG | geolocation | 7 |
| `santo agostinho` | PE | geolocation | 7 |
| `sucatinga` | CE | geolocation | 7 |
| `adhemar de barros` | PR | customers, geolocation | 6 |
| `agisse` | SP | customers, geolocation | 6 |
| `aguas claras` | RS | customers, geolocation | 6 |
| `barao ataliba nogueira` | SP | customers, geolocation | 6 |
| `conrado` | RJ | customers, geolocation | 6 |
| `desembargador otoni` | MG | customers, geolocation | 6 |
| `ipiabas` | RJ | customers, geolocation | 6 |
| `itaguacu` | GO | customers, geolocation | 6 |
| `jacigua` | ES | customers, geolocation | 6 |
| `ravena` | MG | customers, geolocation | 6 |
| `sacra familia do tingua` | RJ | customers, geolocation | 6 |
| `santa isabel do rio preto` | RJ | customers, geolocation | 6 |
| `santa maria` | RJ | customers, geolocation | 6 |
| `sucesso` | CE | customers, geolocation | 6 |
| `taperuaba` | CE | customers, geolocation | 6 |
| `travessao` | RJ | customers, geolocation | 6 |
| `visconde de maua` | RJ | customers, geolocation | 6 |
| `guarizinho` | SP | geolocation | 6 |
| `lajinha` | ES | geolocation | 6 |
| `rive` | ES | geolocation | 6 |
| `sana` | RJ | geolocation | 6 |
| `santa rita de ouro preto` | MG | geolocation | 6 |
| `santa rita durao` | MG | geolocation | 6 |
| `alto alegre do iguacu` | PR | customers, geolocation | 5 |
| `boa esperanca` | RJ | customers, geolocation | 5 |
| `central de santa helena` | MG | customers, geolocation | 5 |
| `conceicao da ibitipoca` | MG | customers, geolocation | 5 |
| `mutum parana` | RO | customers, geolocation | 5 |
| `padre gonzales` | RS | customers, geolocation | 5 |
| `purilandia` | RJ | customers, geolocation | 5 |
| `santana do capivari` | MG | customers, geolocation | 5 |
| `sao domingos` | MG | customers, geolocation | 5 |
| `vargem grande do soturno` | ES | customers, geolocation | 5 |
| `alberto isaacson` | MG | geolocation | 5 |
| `borda do campo` | PR | geolocation | 5 |
| `braço do rio` | ES | geolocation | 5 |
| `campos de cunha` | SP | geolocation | 5 |
| `estacao cocal` | SC | geolocation | 5 |
| `floresta` | MG | geolocation | 5 |
| `frutal do campo` | SP | geolocation | 5 |
| `jurucê` | SP | geolocation | 5 |
| `nossa senhora da aparecida` | RJ | geolocation | 5 |
| `nova esperanca` | MG | geolocation | 5 |
| `ouro verde do piquiri` | PR | geolocation | 5 |
| `santo antonio do leite` | MG | geolocation | 5 |
| `são josé do itueto` | MG | geolocation | 5 |
| `são vicente de paula` | RJ | geolocation | 5 |
| `vista alegre` | MG | geolocation | 5 |
| `anhandui` | MS | customers, geolocation | 4 |
| `antunes` | MG | customers, geolocation | 4 |
| `araguaia` | ES | customers, geolocation | 4 |
| `botelho` | SP | customers, geolocation | 4 |
| `engenheiro balduino` | SP | customers, geolocation | 4 |
| `engenheiro passos` | RJ | customers, geolocation | 4 |
| `flores` | CE | customers, geolocation | 4 |
| `jamaica` | SP | customers, geolocation | 4 |
| `morro vermelho` | MG | customers, geolocation | 4 |
| `santa cruz do prata` | MG | customers, geolocation | 4 |
| `santa cruz do timbo` | SC | customers, geolocation | 4 |
| `santa rita da floresta` | RJ | customers, geolocation | 4 |
| `santo antonio do canaa` | ES | customers, geolocation | 4 |
| `sao geraldo do baguari` | MG | customers, geolocation | 4 |
| `sao goncalo do rio das pedras` | MG | customers, geolocation | 4 |
| `sao joao do sobrado` | ES | customers, geolocation | 4 |
| `sao sebastiao de campos` | RJ | customers, geolocation | 4 |
| `sapucaia` | MG | customers, geolocation | 4 |
| `tocos` | RJ | customers, geolocation | 4 |
| `vila nelita` | ES | customers, geolocation | 4 |
| `vila reis` | PR | customers, geolocation | 4 |
| `alegria` | MG | geolocation | 4 |
| `candia` | SP | geolocation | 4 |
| `cangas` | MT | geolocation | 4 |
| `conceicao de jacarei` | RJ | geolocation | 4 |
| `conceicao do capim` | MG | geolocation | 4 |
| `conservatória` | RJ | geolocation | 4 |
| `correntinho` | MG | geolocation | 4 |
| `costas da mantiqueira` | MG | geolocation | 4 |
| `divino espirito santo` | MG | geolocation | 4 |
| `inhomirim` | RJ | geolocation | 4 |
| `ipituna` | RJ | geolocation | 4 |
| `isabel` | ES | geolocation | 4 |
| `jacaré` | SP | geolocation | 4 |
| `jafa` | SP | geolocation | 4 |
| `lamounier` | MG | geolocation | 4 |
| `luizlândia do oeste` | MG | geolocation | 4 |
| `lídice` | RJ | geolocation | 4 |
| `milho verde` | MG | geolocation | 4 |
| `monsenhor horta` | MG | geolocation | 4 |
| `monte alegre` | RJ | geolocation | 4 |
| `nova casa verde` | MS | geolocation | 4 |
| `pecem` | CE | geolocation | 4 |
| `retiro do muriae` | RJ | geolocation | 4 |
| `santa clara` | RJ | geolocation | 4 |
| `santo aleixo` | RJ | geolocation | 4 |
| `sao benedito das areias` | SP | geolocation | 4 |
| `sao francisco da praia` | SP | geolocation | 4 |
| `sao joao da serra negra` | MG | geolocation | 4 |
| `sao sebastiao do pontal` | MG | geolocation | 4 |
| `senador mourao` | MG | geolocation | 4 |
| `sereno` | MG | geolocation | 4 |
| `vila nova de campos` | RJ | geolocation | 4 |
| `alexandra` | PR | customers, geolocation | 3 |
| `angustura` | MG | customers, geolocation | 3 |
| `campo alegre de minas` | MG | customers, geolocation | 3 |
| `capao da porteira` | RS | customers, geolocation | 3 |
| `chaveslandia` | MG | customers, geolocation | 3 |
| `ibiajara` | BA | customers, geolocation | 3 |
| `ibitira` | BA | customers, geolocation | 3 |
| `lagoa do mato` | CE | customers, geolocation | 3 |
| `pacotuba` | ES | customers, geolocation | 3 |
| `piao` | RJ | customers, geolocation | 3 |
| `pocoes de paineiras` | MG | customers, geolocation | 3 |
| `ponto do marambaia` | MG | customers, geolocation | 3 |
| `queixada` | MG | customers, geolocation | 3 |
| `quilometro 14 do mutum` | ES | customers, geolocation | 3 |
| `rainha do mar` | RS | customers, geolocation | 3 |
| `sanga puita` | MS | customers, geolocation | 3 |
| `santo antonio das queimadas` | PE | customers, geolocation | 3 |
| `sao domingos` | PE | customers, geolocation | 3 |
| `sede alvorada` | PR | customers, geolocation | 3 |
| `serra bonita` | MG | customers, geolocation | 3 |
| `tecainda` | SP | customers, geolocation | 3 |
| `venda branca` | SP | customers, geolocation | 3 |
| `agulha` | SP | geolocation | 3 |
| `alfredo guedes` | SP | geolocation | 3 |
| `baguacu` | SP | geolocation | 3 |
| `barão ataliba nogueira` | SP | geolocation | 3 |
| `barão de juparana` | RJ | geolocation | 3 |
| `bentopolis` | PR | geolocation | 3 |
| `bragantina` | PR | geolocation | 3 |
| `costa machado` | SP | geolocation | 3 |
| `crisolia` | MG | geolocation | 3 |
| `cuiaba paulista` | SP | geolocation | 3 |
| `cumuruxatiba` | BA | geolocation | 3 |
| `dalbergia` | SC | geolocation | 3 |
| `domelia` | SP | geolocation | 3 |
| `floresta do sul` | SP | geolocation | 3 |
| `frade` | RJ | geolocation | 3 |
| `ibirajá` | BA | geolocation | 3 |
| `igaraí` | SP | geolocation | 3 |
| `inoa` | RJ | geolocation | 3 |
| `itapocu` | SC | geolocation | 3 |
| `itupeva` | BA | geolocation | 3 |
| `jaibaras` | CE | geolocation | 3 |
| `jamapará` | RJ | geolocation | 3 |
| `jansen` | RS | geolocation | 3 |
| `juruce` | SP | geolocation | 3 |
| `lagoa branca` | SP | geolocation | 3 |
| `limeira de mantena` | MG | geolocation | 3 |
| `manuel duarte` | RJ | geolocation | 3 |
| `monsenhor joao alexandre` | MG | geolocation | 3 |
| `monte sinai` | ES | geolocation | 3 |
| `nossa senhora do ó` | PE | geolocation | 3 |
| `nova america` | SP | geolocation | 3 |
| `nova milano` | RS | geolocation | 3 |
| `padre fialho` | MG | geolocation | 3 |
| `paulista` | ES | geolocation | 3 |
| `pinhal alto` | RS | geolocation | 3 |
| `polvilho` | SP | geolocation | 3 |
| `rocas novas` | MG | geolocation | 3 |
| `santa eliza` | PR | geolocation | 3 |
| `santa terezinha de minas` | MG | geolocation | 3 |
| `sao jose do itueto` | MG | geolocation | 3 |
| `sao pedro` | MS | geolocation | 3 |
| `sao sebastiao de braunas` | MG | geolocation | 3 |
| `serra do vento` | PE | geolocation | 3 |
| `são benedito das areias` | SP | geolocation | 3 |
| `são joão do paraíso` | RJ | geolocation | 3 |
| `são sebastião do pontal` | MG | geolocation | 3 |
| `são vicente` | MG | geolocation | 3 |
| `vista alegre do abuna` | RO | geolocation | 3 |
| `amanari` | CE | customers, geolocation | 2 |
| `andrequice` | MG | customers, geolocation | 2 |
| `baguari` | MG | customers, geolocation | 2 |
| `bandeirantes d'oeste` | SP | customers, geolocation | 2 |
| `boa ventura` | RJ | customers, geolocation | 2 |
| `brejo bonito` | MG | customers, geolocation | 2 |
| `cambiasca` | RJ | customers, geolocation | 2 |
| `carnaiba do sertao` | BA | customers, geolocation | 2 |
| `domiciano ribeiro` | GO | customers | 2 |
| `fonseca` | MG | customers, geolocation | 2 |
| `fragosos` | SC | customers, geolocation | 2 |
| `guarapua` | SP | customers, geolocation | 2 |
| `guariroba` | SP | customers | 2 |
| `guassusse` | CE | customers, geolocation | 2 |
| `lages` | CE | customers, geolocation | 2 |
| `mariental` | PR | customers, geolocation | 2 |
| `martinesia` | MG | customers, geolocation | 2 |
| `mendonca` | MG | customers, geolocation | 2 |
| `monnerat` | RJ | customers | 2 |
| `monte alverne` | RS | customers, geolocation | 2 |
| `monte bonito` | RS | customers, geolocation | 2 |
| `nossa senhora do remedio` | SP | customers | 2 |
| `osvaldo kroeff` | RS | customers, geolocation | 2 |
| `palmeirinha` | PR | customers | 2 |
| `paraju` | ES | customers, geolocation | 2 |
| `pedra menina` | MG | customers, geolocation | 2 |
| `prudencio thomaz` | MS | customers, geolocation | 2 |
| `ribeiro junqueira` | MG | customers, geolocation | 2 |
| `rio verde` | PR | customers, geolocation | 2 |
| `santo eduardo` | RJ | customers | 2 |
| `sao joao de petropolis` | ES | customers, geolocation | 2 |
| `sao jose do ribeirao` | RJ | customers, geolocation | 2 |
| `sao mateus de minas` | MG | customers, geolocation | 2 |
| `serra dos dourados` | PR | customers, geolocation | 2 |
| `silvano` | MG | customers, geolocation | 2 |
| `silveira carvalho` | MG | customers, geolocation | 2 |
| `termas de ibira` | SP | customers, geolocation | 2 |
| `tres irmaos` | RJ | customers, geolocation | 2 |
| `tuparece` | MG | customers, geolocation | 2 |
| `valao do barro` | RJ | customers, geolocation | 2 |
| `vermelho` | MG | customers, geolocation | 2 |
| `vitorinos` | MG | customers, geolocation | 2 |
| `aguas ferreas` | MG | geolocation | 2 |
| `alvacao` | MG | geolocation | 2 |
| `alvorada` | MG | geolocation | 2 |
| `americano` | PA | geolocation | 2 |
| `antônio pereira` | MG | geolocation | 2 |
| `aparecida de são manuel` | SP | geolocation | 2 |
| `arapua` | MS | geolocation | 2 |
| `aurora do iguacu` | PR | geolocation | 2 |
| `barra do ariranha` | MG | geolocation | 2 |
| `barra do cuiete` | MG | geolocation | 2 |
| `barro duro` | MA | geolocation | 2 |
| `batateira` | PE | geolocation | 2 |
| `benfica` | PA | geolocation | 2 |
| `bitupita` | CE | geolocation | 2 |
| `boa esperança` | RJ | geolocation | 2 |
| `boa uniao de itabirinha` | MG | geolocation | 2 |
| `boa união de itabirinha` | MG | geolocation | 2 |
| `boa vista de minas` | MG | geolocation | 2 |
| `brasitania` | SP | geolocation | 2 |
| `burarama` | ES | geolocation | 2 |
| `caetano mendes` | PR | geolocation | 2 |
| `califórnia da barra` | RJ | geolocation | 2 |
| `calixto` | MG | geolocation | 2 |
| `capao novo` | RS | geolocation | 2 |
| `carabucu` | RJ | geolocation | 2 |
| `castelo dos sonhos` | PA | geolocation | 2 |
| `catucaba` | SP | geolocation | 2 |
| `claudio manuel` | MG | geolocation | 2 |
| `clevelandia do norte` | AP | geolocation | 2 |
| `colonia nova` | RS | geolocation | 2 |
| `colônia` | RJ | geolocation | 2 |
| `conceição de jacareí` | RJ | geolocation | 2 |
| `conduru` | ES | geolocation | 2 |
| `cristalina` | MS | geolocation | 2 |
| `cruzeiro do norte` | PR | geolocation | 2 |
| `cruzes` | PE | geolocation | 2 |
| `curupa` | SP | geolocation | 2 |
| `dez de maio` | PR | geolocation | 2 |
| `divino espírito santo` | MG | geolocation | 2 |
| `dois de abril` | MG | geolocation | 2 |
| `dores do paraibuna` | MG | geolocation | 2 |
| `doutor oliveira castro` | PR | geolocation | 2 |
| `estação cocal` | SC | geolocation | 2 |
| `esteios` | MG | geolocation | 2 |
| `goiabal` | MG | geolocation | 2 |
| `granada` | MG | geolocation | 2 |
| `guardinha` | MG | geolocation | 2 |
| `guia de pacobaiba` | RJ | geolocation | 2 |
| `honorópolis` | MG | geolocation | 2 |
| `icara` | PR | geolocation | 2 |
| `ipoema` | MG | geolocation | 2 |
| `iraporanga` | BA | geolocation | 2 |
| `irundiara` | BA | geolocation | 2 |
| `itabaiana` | ES | geolocation | 2 |
| `itacurussá` | RJ | geolocation | 2 |
| `itapiru` | MG | geolocation | 2 |
| `jabitaca` | PE | geolocation | 2 |
| `jacuba` | SP | geolocation | 2 |
| `juritis` | SP | geolocation | 2 |
| `luar` | PR | geolocation | 2 |
| `lucaia` | BA | geolocation | 2 |
| `luminosa` | MG | geolocation | 2 |
| `mangabeira` | CE | geolocation | 2 |
| `mocambeiro` | MG | geolocation | 2 |
| `monte verde paulista` | SP | geolocation | 2 |
| `montese` | MS | geolocation | 2 |
| `morro do coco` | RJ | geolocation | 2 |
| `naque-nanuque` | MG | geolocation | 2 |
| `neolandia` | MG | geolocation | 2 |
| `nova alexandria` | SP | geolocation | 2 |
| `nova california` | RO | geolocation | 2 |
| `nova floresta` | CE | geolocation | 2 |
| `nova itapirema` | SP | geolocation | 2 |
| `nova patria` | SP | geolocation | 2 |
| `nova sardenha` | RS | geolocation | 2 |
| `otavio rocha` | RS | geolocation | 2 |
| `paraiso do tobias` | RJ | geolocation | 2 |
| `paruru` | SP | geolocation | 2 |
| `passagem dos teixeiras` | BA | geolocation | 2 |
| `penha do capim` | MG | geolocation | 2 |
| `perpétuo socorro` | MG | geolocation | 2 |
| `piacatuba` | MG | geolocation | 2 |
| `pilar` | MG | geolocation | 2 |
| `pirituba` | PE | geolocation | 2 |
| `pontinha do cocho` | MS | geolocation | 2 |
| `porto mendes` | PR | geolocation | 2 |
| `porto sao jose` | PR | geolocation | 2 |
| `prudêncio thomaz` | MS | geolocation | 2 |
| `rainha isabel` | PE | geolocation | 2 |
| `rio das mortes` | MG | geolocation | 2 |
| `rodrigo silva` | MG | geolocation | 2 |
| `salgadalia` | BA | geolocation | 2 |
| `santa luzia de mantenopolis` | ES | geolocation | 2 |
| `santa zelia` | PR | geolocation | 2 |
| `santana de patos` | MG | geolocation | 2 |
| `santo antonio do rio verde` | GO | geolocation | 2 |
| `santo antônio do rio verde` | GO | geolocation | 2 |
| `santo antônio dos campos` | MG | geolocation | 2 |
| `sao joao de itaguacu` | SP | geolocation | 2 |
| `sao joao do jacutinga` | MG | geolocation | 2 |
| `sao jose do torto` | CE | geolocation | 2 |
| `sao martinho` | PR | geolocation | 2 |
| `sao roque da fartura` | SP | geolocation | 2 |
| `sao sebastiao da barra` | MG | geolocation | 2 |
| `sao sebastiao da vitoria` | MG | geolocation | 2 |
| `sao vicente` | MG | geolocation | 2 |
| `sao vicente do rio doce` | MG | geolocation | 2 |
| `sapucaia de guanhaes` | MG | geolocation | 2 |
| `sapucaia do norte` | MG | geolocation | 2 |
| `são josé da mata` | PB | geolocation | 2 |
| `são sebastião da vala` | MG | geolocation | 2 |
| `são sebastião do sacramento` | MG | geolocation | 2 |
| `sítio grande` | BA | geolocation | 2 |
| `tebas` | MG | geolocation | 2 |
| `vau-acu` | MG | geolocation | 2 |
| `vermelho velho` | MG | geolocation | 2 |
| `vidigal` | PR | geolocation | 2 |
| `vila vargas` | MS | geolocation | 2 |
| `vila verde` | ES | geolocation | 2 |
| `ajapi` | SP | customers | 1 |
| `angelo frechiani` | ES | customers | 1 |
| `aribice` | BA | customers | 1 |
| `bemposta` | RJ | customers | 1 |
| `bom jesus do querendo` | RJ | customers | 1 |
| `cipo-guacu` | SP | customers | 1 |
| `conceicao do formoso` | MG | customers | 1 |
| `corrego do ouro` | RJ | customers | 1 |
| `doce grande` | PR | customers | 1 |
| `dourado` | CE | customers | 1 |
| `estevao de araujo` | MG | customers | 1 |
| `glaura` | MG | customers | 1 |
| `guinda` | MG | customers | 1 |
| `humildes` | BA | customers | 1 |
| `ibitioca` | RJ | customers | 1 |
| `ipiranga` | RS | customers | 1 |
| `jacuipe` | BA | customers | 1 |
| `jaguarembe` | RJ | customers | 1 |
| `major porto` | MG | customers | 1 |
| `missi` | CE | customers | 1 |
| `mussurepe` | RJ | customers | 1 |
| `palmital de minas` | MG | customers | 1 |
| `perola independente` | PR | customers | 1 |
| `piacu` | ES | customers | 1 |
| `pinheiros` | SP | customers | 1 |
| `pinhotiba` | MG | customers | 1 |
| `santa margarida` | PR | customers | 1 |
| `santana` | PR | customers | 1 |
| `sao benedito` | MG | customers | 1 |
| `sao clemente` | PR | customers | 1 |
| `sao francisco do humaita` | MG | customers | 1 |
| `sao miguel do cambui` | PR | customers | 1 |
| `sao sebastiao da serra` | SP | customers | 1 |
| `sao sebastiao do paraiba` | RJ | customers | 1 |
| `sao vitor` | MG | customers | 1 |
| `siriji` | PE | customers | 1 |
| `taboquinhas` | BA | customers | 1 |
| `pirituba` | SP | sellers | 1 |
| `vicente de carvalho` | SP | sellers | 1 |
| `abreus` | MG | geolocation | 1 |
| `acioli` | ES | geolocation | 1 |
| `acupe` | BA | geolocation | 1 |
| `adao colares` | MG | geolocation | 1 |
| `afonso arinos` | RJ | geolocation | 1 |
| `agua branca de minas` | MG | geolocation | 1 |
| `agua vermelha` | SP | geolocation | 1 |
| `aldeia` | MG | geolocation | 1 |
| `algodões` | BA | geolocation | 1 |
| `alto calcado` | ES | geolocation | 1 |
| `alto maranhao` | MG | geolocation | 1 |
| `alto mutum preto` | ES | geolocation | 1 |
| `amandina` | MS | geolocation | 1 |
| `amanhece` | MG | geolocation | 1 |
| `ana dias` | SP | geolocation | 1 |
| `anguereta` | MG | geolocation | 1 |
| `aparecida de minas` | MG | geolocation | 1 |
| `apeu` | PA | geolocation | 1 |
| `arco verde` | RS | geolocation | 1 |
| `avaí do jacinto` | MG | geolocation | 1 |
| `azambuja` | SC | geolocation | 1 |
| `açu da torre` | BA | geolocation | 1 |
| `bandeirantes` | MG | geolocation | 1 |
| `banquete` | RJ | geolocation | 1 |
| `barra feliz` | MG | geolocation | 1 |
| `barreiro branco` | MG | geolocation | 1 |
| `batinga` | BA | geolocation | 1 |
| `bentópolis de minas` | MG | geolocation | 1 |
| `bicuiba` | MG | geolocation | 1 |
| `bizarra` | PE | geolocation | 1 |
| `boa sorte` | RJ | geolocation | 1 |
| `boa uniao` | BA | geolocation | 1 |
| `boa vista` | MT | geolocation | 1 |
| `boa vista dos andradas` | SP | geolocation | 1 |
| `bom fim do bom jesus` | SP | geolocation | 1 |
| `bom jardim do sul` | PR | geolocation | 1 |
| `bom retiro da esperanca` | SP | geolocation | 1 |
| `brasitânia` | SP | geolocation | 1 |
| `bugre` | PR | geolocation | 1 |
| `buriti` | RS | geolocation | 1 |
| `cacaratiba` | MG | geolocation | 1 |
| `cacarema` | MG | geolocation | 1 |
| `cachoeira alegre` | MG | geolocation | 1 |
| `cachoeira de santa cruz` | MG | geolocation | 1 |
| `cafe` | ES | geolocation | 1 |
| `caicara` | CE | geolocation | 1 |
| `calheiros` | RJ | geolocation | 1 |
| `camela` | PE | geolocation | 1 |
| `campinal` | SP | geolocation | 1 |
| `campinas` | AC | geolocation | 1 |
| `canabrava` | MG | geolocation | 1 |
| `caponga` | CE | geolocation | 1 |
| `caporanga` | SP | geolocation | 1 |
| `carabuçu` | RJ | geolocation | 1 |
| `cardeal` | SP | geolocation | 1 |
| `cataguarino` | MG | geolocation | 1 |
| `catingal` | BA | geolocation | 1 |
| `catune` | MG | geolocation | 1 |
| `catuni` | MG | geolocation | 1 |
| `caçarema` | MG | geolocation | 1 |
| `cipolandia` | MS | geolocation | 1 |
| `cisneiros` | MG | geolocation | 1 |
| `clevelândia do norte` | AP | geolocation | 1 |
| `colonia` | RJ | geolocation | 1 |
| `colorado do norte` | MT | geolocation | 1 |
| `colônia nova` | RS | geolocation | 1 |
| `conceição` | SP | geolocation | 1 |
| `conceição de tronqueiras` | MG | geolocation | 1 |
| `conceição do capim` | MG | geolocation | 1 |
| `congonhas` | PR | geolocation | 1 |
| `corrego dos monos` | ES | geolocation | 1 |
| `cristal do norte` | ES | geolocation | 1 |
| `cuiabá paulista` | SP | geolocation | 1 |
| `curumim` | RS | geolocation | 1 |
| `córrego do ouro` | MG | geolocation | 1 |
| `córrego dos monos` | ES | geolocation | 1 |
| `deserto` | CE | geolocation | 1 |
| `dois irmãos` | PR | geolocation | 1 |
| `eleuterio` | SP | geolocation | 1 |
| `eleutério` | SP | geolocation | 1 |
| `encantado d'oeste` | PR | geolocation | 1 |
| `eneida` | SP | geolocation | 1 |
| `engenheiro balduíno` | SP | geolocation | 1 |
| `engenheiro franca` | BA | geolocation | 1 |
| `engenheiro schnoor` | MG | geolocation | 1 |
| `engenho do ribeiro` | MG | geolocation | 1 |
| `epaminondas otoni` | MG | geolocation | 1 |
| `esmeraldas de ferros` | MG | geolocation | 1 |
| `estrela da barra` | MG | geolocation | 1 |
| `estrela de jordania` | MG | geolocation | 1 |
| `estrela de jordânia` | MG | geolocation | 1 |
| `fazenda nova` | PE | geolocation | 1 |
| `fazenda souza` | RS | geolocation | 1 |
| `feiticeiro` | CE | geolocation | 1 |
| `ferruginha` | MG | geolocation | 1 |
| `freguesia do andira` | AM | geolocation | 1 |
| `furquim` | MG | geolocation | 1 |
| `gardenia` | SP | geolocation | 1 |
| `getulândia` | RJ | geolocation | 1 |
| `gororos` | MG | geolocation | 1 |
| `gororós` | MG | geolocation | 1 |
| `governador lacerda de aguiar` | ES | geolocation | 1 |
| `graciosa` | PR | geolocation | 1 |
| `gramadinho` | SP | geolocation | 1 |
| `grota` | MG | geolocation | 1 |
| `guaianas` | SP | geolocation | 1 |
| `guaicui` | MG | geolocation | 1 |
| `guaipora` | PR | geolocation | 1 |
| `guaporanga` | SC | geolocation | 1 |
| `guassussê` | CE | geolocation | 1 |
| `guaxima` | MG | geolocation | 1 |
| `guia de pacobaíba` | RJ | geolocation | 1 |
| `ibicua` | CE | geolocation | 1 |
| `ibitiranga` | PE | geolocation | 1 |
| `ibo` | BA | geolocation | 1 |
| `iguaibi` | BA | geolocation | 1 |
| `independencia` | MG | geolocation | 1 |
| `inubia` | BA | geolocation | 1 |
| `inúbia` | BA | geolocation | 1 |
| `ipuca` | RJ | geolocation | 1 |
| `irapé` | SP | geolocation | 1 |
| `itaim` | MG | geolocation | 1 |
| `itaimbe` | ES | geolocation | 1 |
| `itapirucu` | MG | geolocation | 1 |
| `itaquarai` | BA | geolocation | 1 |
| `itaunas` | ES | geolocation | 1 |
| `iubatinga` | SP | geolocation | 1 |
| `ivailandia` | PR | geolocation | 1 |
| `jacilandia` | GO | geolocation | 1 |
| `jangada` | PR | geolocation | 1 |
| `jordanésia` | SP | geolocation | 1 |
| `jordao` | CE | geolocation | 1 |
| `joão amaro` | BA | geolocation | 1 |
| `juatama` | CE | geolocation | 1 |
| `jurupema` | SP | geolocation | 1 |
| `lagoinha` | CE | geolocation | 1 |
| `laje grande` | PE | geolocation | 1 |
| `laranjais` | RJ | geolocation | 1 |
| `lavras novas` | MG | geolocation | 1 |
| `luiz pires de minas` | MG | geolocation | 1 |
| `maiauata` | PA | geolocation | 1 |
| `maniacu` | BA | geolocation | 1 |
| `mantiqueira do palmital` | MG | geolocation | 1 |
| `marambainha` | MG | geolocation | 1 |
| `martinho prado junior` | SP | geolocation | 1 |
| `martins guimaraes` | MG | geolocation | 1 |
| `melo viana` | MG | geolocation | 1 |
| `menino jesus` | BA | geolocation | 1 |
| `mercês de água limpa` | MG | geolocation | 1 |
| `mineirolândia` | CE | geolocation | 1 |
| `morro chato` | SC | geolocation | 1 |
| `mucuri` | MG | geolocation | 1 |
| `nelson de sena` | MG | geolocation | 1 |
| `neolândia` | MG | geolocation | 1 |
| `nossa senhora da luz` | PE | geolocation | 1 |
| `nova américa` | SP | geolocation | 1 |
| `nova santa luzia` | MG | geolocation | 1 |
| `novo sobradinho` | PR | geolocation | 1 |
| `olhos d'agua do oeste` | MG | geolocation | 1 |
| `ouroana` | GO | geolocation | 1 |
| `paiquere` | PR | geolocation | 1 |
| `palmeiral` | MG | geolocation | 1 |
| `paraná d'oeste` | PR | geolocation | 1 |
| `parapeuna` | RJ | geolocation | 1 |
| `passa três` | RJ | geolocation | 1 |
| `passé` | BA | geolocation | 1 |
| `pedro versiani` | MG | geolocation | 1 |
| `perdilandia` | MG | geolocation | 1 |
| `perpétuo socorro` | PE | geolocation | 1 |
| `petunia` | MG | geolocation | 1 |
| `piedade do paraopeba` | MG | geolocation | 1 |
| `pindurão` | PB | geolocation | 1 |
| `pinheiro grosso` | MG | geolocation | 1 |
| `pinheiros altos` | MG | geolocation | 1 |
| `pioneiros` | SP | geolocation | 1 |
| `piramboia` | SP | geolocation | 1 |
| `pirapora` | MS | geolocation | 1 |
| `ponte alta de minas` | MG | geolocation | 1 |
| `porto de cima` | PR | geolocation | 1 |
| `porto velho do cunha` | RJ | geolocation | 1 |
| `potunduva` | SP | geolocation | 1 |
| `poxim` | AL | geolocation | 1 |
| `presidente pena` | MG | geolocation | 1 |
| `pulinopolis` | PR | geolocation | 1 |
| `queimados` | CE | geolocation | 1 |
| `quilombo` | RS | geolocation | 1 |
| `quinta` | RS | geolocation | 1 |
| `quintinos` | MG | geolocation | 1 |
| `rafael arruda` | CE | geolocation | 1 |
| `rajada` | PE | geolocation | 1 |
| `residencia fuck` | SC | geolocation | 1 |
| `retiro do muriaé` | RJ | geolocation | 1 |
| `ribeirao de sao domingos` | MG | geolocation | 1 |
| `ribeirão de são domingos` | MG | geolocation | 1 |
| `rio bonito` | PR | geolocation | 1 |
| `rio bonito` | SC | geolocation | 1 |
| `rio do meio` | BA | geolocation | 1 |
| `rio do salto` | PR | geolocation | 1 |
| `rio melo` | MG | geolocation | 1 |
| `riverlandia` | GO | geolocation | 1 |
| `roberto` | SP | geolocation | 1 |
| `rosario de minas` | MG | geolocation | 1 |
| `rosario do pontal` | MG | geolocation | 1 |
| `roseiral` | MG | geolocation | 1 |
| `rubiao junior` | SP | geolocation | 1 |
| `sacra família do tinguá` | RJ | geolocation | 1 |
| `sampaio correia` | RJ | geolocation | 1 |
| `santa elvira` | MT | geolocation | 1 |
| `santa eudóxia` | SP | geolocation | 1 |
| `santa lucia do piai` | RS | geolocation | 1 |
| `santa luzia` | RS | geolocation | 1 |
| `santa luzia de caratinga` | MG | geolocation | 1 |
| `santa luzia do cariri` | PB | geolocation | 1 |
| `santa rita do cedro` | MG | geolocation | 1 |
| `santa rita durão` | MG | geolocation | 1 |
| `santana de caldas` | MG | geolocation | 1 |
| `santana do paraopeba` | MG | geolocation | 1 |
| `santana do tabuleiro` | MG | geolocation | 1 |
| `santelmo` | SP | geolocation | 1 |
| `santo agostinho` | ES | geolocation | 1 |
| `santo antonio do manhuacu` | MG | geolocation | 1 |
| `santo antonio do norte` | MG | geolocation | 1 |
| `santo antonio do pirapetinga` | MG | geolocation | 1 |
| `santo antônio das queimadas` | PE | geolocation | 1 |
| `santo antônio do canaã` | ES | geolocation | 1 |
| `santo antônio do leite` | MG | geolocation | 1 |
| `sao bartolomeu` | MG | geolocation | 1 |
| `sao benedito da cachoeirinha` | SP | geolocation | 1 |
| `sao goncalo de botelhos` | MG | geolocation | 1 |
| `sao joao da chapada` | MG | geolocation | 1 |
| `sao joao da fortaleza` | BA | geolocation | 1 |
| `sao joao da serra` | MG | geolocation | 1 |
| `sao joao de deus` | CE | geolocation | 1 |
| `sao joao de vicosa` | ES | geolocation | 1 |
| `sao jose` | MS | geolocation | 1 |
| `sao jose da mata` | PB | geolocation | 1 |
| `sao jose das laranjeiras` | SP | geolocation | 1 |
| `sao jose das torres` | ES | geolocation | 1 |
| `sao jose do acacio` | MG | geolocation | 1 |
| `sao jose do itavo` | PR | geolocation | 1 |
| `sao jose do ivai` | PR | geolocation | 1 |
| `sao jose dos salgados` | MG | geolocation | 1 |
| `sao manoel do guaiacu` | MG | geolocation | 1 |
| `sao miguel` | CE | geolocation | 1 |
| `sao pedro` | CE | geolocation | 1 |
| `sao pedro` | PE | geolocation | 1 |
| `sao roque do chopim` | PR | geolocation | 1 |
| `sao roque do paraguacu` | BA | geolocation | 1 |
| `sao sebastiao da vala` | MG | geolocation | 1 |
| `sao sebastiao dos pocoes` | MG | geolocation | 1 |
| `sao silvestre` | PR | geolocation | 1 |
| `sao vicente da estrela` | MG | geolocation | 1 |
| `sao vicente do grama` | MG | geolocation | 1 |
| `sapiranga` | SC | geolocation | 1 |
| `sarandira` | MG | geolocation | 1 |
| `sebastiao de abreu` | CE | geolocation | 1 |
| `senhora do carmo` | MG | geolocation | 1 |
| `serra azul` | MG | geolocation | 1 |
| `serra da tapuia` | RN | geolocation | 1 |
| `simoes` | SP | geolocation | 1 |
| `socavao` | PR | geolocation | 1 |
| `sodrelia` | SP | geolocation | 1 |
| `sonho azul` | MT | geolocation | 1 |
| `são camilo` | PR | geolocation | 1 |
| `são domingos` | PE | geolocation | 1 |
| `são francisco da praia` | SP | geolocation | 1 |
| `são francisco xavier` | SP | geolocation | 1 |
| `são gonçalo de botelhos` | MG | geolocation | 1 |
| `são josé das laranjeiras` | SP | geolocation | 1 |
| `são josé do barreiro` | MG | geolocation | 1 |
| `são josé do torto` | CE | geolocation | 1 |
| `são josé do turvo` | RJ | geolocation | 1 |
| `são joão de itaguaçu` | SP | geolocation | 1 |
| `são martinho` | PR | geolocation | 1 |
| `são pedro de rates` | ES | geolocation | 1 |
| `são pedro do avaí` | MG | geolocation | 1 |
| `são sebastião da vitória` | MG | geolocation | 1 |
| `são sebastião dos torres` | MG | geolocation | 1 |
| `tabuao` | MG | geolocation | 1 |
| `tapuirama` | MG | geolocation | 1 |
| `tauape` | BA | geolocation | 1 |
| `tocandira` | MG | geolocation | 1 |
| `topazio` | MG | geolocation | 1 |
| `torneiros` | MG | geolocation | 1 |
| `tres aliancas` | SP | geolocation | 1 |
| `ubauna` | PR | geolocation | 1 |
| `ubiraita` | BA | geolocation | 1 |
| `vale dos vinhedos` | RS | geolocation | 1 |
| `vera cruz de minas` | MG | geolocation | 1 |
| `veredas` | MG | geolocation | 1 |
| `vila nova de minas` | MG | geolocation | 1 |
| `vinhatico` | ES | geolocation | 1 |
| `visconde de imbe` | RJ | geolocation | 1 |
| `vista alegre` | MS | geolocation | 1 |
| `água boa` | PR | geolocation | 1 |
| `água fria` | PE | geolocation | 1 |

---

## Section 3 — Fuzzy suggestion available

168 pairs did not match at município or distrito level,
but fuzzy matching found a município candidate with similarity ≥ 0.85 in the same state.
These are likely spelling variants, hyphenation differences, or typos of known municipalities.

| Raw city | State | Sources | Affected rows | Suggested correction | Similarity |
|---|---|---|---|---|---|
| `mogi-guacu` | SP | customers, geolocation | 643 | Mogi Guaçu | 0.95 |
| `santana do livramento` | RS | customers, geolocation | 378 | Sant'Ana do Livramento | 0.97 |
| `piumhii` | MG | customers, geolocation | 135 | Piumhi | 0.92 |
| `biritiba-mirim` | SP | customers, geolocation | 120 | Biritiba Mirim | 0.96 |
| `mogi-mirim` | SP | customers, geolocation | 95 | Mogi Mirim | 0.95 |
| `santa barbara d oeste` | SP | customers, geolocation, sellers | 86 | Santa Bárbara d'Oeste | 0.97 |
| `papucaia` | RJ | customers, geolocation | 70 | Sapucaia | 0.88 |
| `espigao do oeste` | RO | customers, geolocation | 60 | Espigão D'Oeste | 0.93 |
| `santa isabel do para` | PA | customers, geolocation | 60 | Santa Izabel do Pará | 0.94 |
| `brasopolis` | MG | customers, geolocation | 45 | Brazópolis | 0.90 |
| `armacao de buzios` | RJ | geolocation | 39 | Armação dos Búzios | 0.90 |
| `sao luis do paraitinga` | SP | customers, geolocation | 26 | São Luiz do Paraitinga | 0.95 |
| `grao para` | SC | customers, geolocation | 24 | Grão-Pará | 0.94 |
| `pindare mirim` | MA | customers, geolocation | 22 | Pindaré-Mirim | 0.96 |
| `holambra ii` | SP | customers, geolocation | 21 | Holambra | 0.89 |
| `eldorado dos carajas` | PA | geolocation | 21 | Eldorado do Carajás | 0.97 |
| `embu guaçu` | SP | geolocation | 21 | Embu-Guaçu | 0.95 |
| `caraiba` | PE | customers, geolocation | 16 | Carnaíba | 0.93 |
| `amparo da serra` | MG | customers, geolocation | 15 | Amparo do Serra | 0.92 |
| `dias d avila` | BA | customers, geolocation | 14 | Dias d'Ávila | 0.95 |
| `florinia` | SP | customers, geolocation | 14 | Florínea | 0.88 |
| `sao thome das letras` | MG | customers, geolocation | 14 | São Tomé das Letras | 0.97 |
| `herval d oeste` | SC | geolocation | 14 | Herval d'Oeste | 0.96 |
| `santo antonio do leverger` | MT | customers, geolocation | 13 | Santo Antônio de Leverger | 0.95 |
| `brasópolis` | MG | geolocation | 13 | Brazópolis | 0.90 |
| `espigão do oeste` | RO | geolocation | 13 | Espigão D'Oeste | 0.93 |
| `couto de magalhaes` | TO | customers, geolocation | 11 | Couto Magalhães | 0.93 |
| `palmeira d oeste` | SP | customers, geolocation | 11 | Palmeira d'Oeste | 0.97 |
| `barao de monte alto` | MG | geolocation | 11 | Barão do Monte Alto | 0.94 |
| `lagoa do itaenga` | PE | geolocation | 11 | Lagoa de Itaenga | 0.93 |
| `santa bárbara doeste` | SP | geolocation | 11 | Santa Bárbara d'Oeste | 0.97 |
| `santa teresinha` | BA | customers, geolocation | 10 | Santa Terezinha | 0.93 |
| `gouvea` | MG | geolocation | 10 | Gouveia | 0.92 |
| `santa rita do ibitipoca` | MG | customers, geolocation | 9 | Santa Rita de Ibitipoca | 0.95 |
| `jequirica` | BA | geolocation | 9 | Jiquiriçá | 0.89 |
| `trajano de morais` | RJ | geolocation | 9 | Trajano de Moraes | 0.93 |
| `itapage` | CE | customers, geolocation | 8 | Itapajé | 0.86 |
| `olhos d'agua` | MG | customers, geolocation | 8 | Olhos-d'Água | 0.96 |
| `embu guacu` | SP | geolocation, sellers | 8 | Embu-Guaçu | 0.95 |
| `são thomé das letras` | MG | geolocation | 8 | São Tomé das Letras | 0.97 |
| `maracana` | SC | customers, geolocation | 7 | Maracajá | 0.88 |
| `quixada` | PE | customers, geolocation | 7 | Quixaba | 0.86 |
| `santa isabel do pará` | PA | geolocation | 7 | Santa Izabel do Pará | 0.94 |
| `estrela d oeste` | SP | customers, geolocation | 6 | Estrela d'Oeste | 0.96 |
| `alta alegre dos parecis` | RO | geolocation | 6 | Alto Alegre dos Parecis | 0.95 |
| `alta floresta do oeste` | RO | geolocation | 6 | Alta Floresta D'Oeste | 0.95 |
| `dias davila` | BA | geolocation | 6 | Dias d'Ávila | 0.95 |
| `iguaraci` | PE | geolocation | 6 | Iguaracy | 0.88 |
| `itapejara d  oeste` | PR | geolocation | 6 | Itapejara d'Oeste | 0.97 |
| `olhos d'água` | MG | geolocation | 6 | Olhos-d'Água | 0.96 |
| `pingo-d agua` | MG | geolocation | 6 | Pingo-d'Água | 0.96 |
| `sem peixe` | MG | geolocation | 6 | Sem-Peixe | 0.94 |
| `sao jorge do oeste` | PR | customers, geolocation | 5 | São Jorge d'Oeste | 0.93 |
| `eldorado dos carajás` | PA | geolocation | 5 | Eldorado do Carajás | 0.97 |
| `mirassol d oeste` | MT | geolocation | 5 | Mirassol d'Oeste | 0.97 |
| `aparecida d oeste` | SP | geolocation | 4 | Aparecida d'Oeste | 0.97 |
| `belem de sao francisco` | PE | geolocation | 4 | Belém do São Francisco | 0.95 |
| `embuguacu` | SP | geolocation | 4 | Embu-Guaçu | 0.95 |
| `guajara mirim` | RO | geolocation | 4 | Guajará-Mirim | 0.96 |
| `mirassol doeste` | MT | geolocation | 4 | Mirassol d'Oeste | 0.97 |
| `olho d agua das flores` | AL | geolocation | 4 | Olho d'Água das Flores | 0.97 |
| `olhos-d agua` | MG | geolocation | 4 | Olhos-d'Água | 0.96 |
| `santa barbara doeste` | SP | geolocation | 4 | Santa Bárbara d'Oeste | 0.97 |
| `bataipora` | MS | customers, geolocation | 3 | Batayporã | 0.89 |
| `dias dávila` | BA | geolocation | 3 | Dias d'Ávila | 0.95 |
| `estrela doeste` | SP | geolocation | 3 | Estrela d'Oeste | 0.96 |
| `florínia` | SP | geolocation | 3 | Florínea | 0.88 |
| `nova brasilandia d oeste` | RO | geolocation | 3 | Nova Brasilândia D'Oeste | 0.98 |
| `santa clara d oeste` | SP | geolocation | 3 | Santa Clara d'Oeste | 0.97 |
| `santa luzia doeste` | RO | geolocation | 3 | Santa Luzia D'Oeste | 0.97 |
| `santa rita do oeste` | PR | geolocation | 3 | Santa Maria do Oeste | 0.91 |
| `sao joao do pau d alho` | SP | geolocation | 3 | São João do Pau d'Alho | 0.97 |
| `sao jorge doeste` | PR | geolocation | 3 | São Jorge d'Oeste | 0.97 |
| `sao roque do cannaa` | ES | geolocation | 3 | São Roque do Canaã | 0.97 |
| `santa barbara d´oeste` | SP | sellers | 2 | Santa Bárbara d'Oeste | 0.97 |
| `couto de magalhães` | TO | geolocation | 2 | Couto Magalhães | 0.93 |
| `diamante d  oeste` | PR | geolocation | 2 | Diamante D'Oeste | 0.97 |
| `figueiropolis d oeste` | MT | geolocation | 2 | Figueirópolis D'Oeste | 0.97 |
| `figueiropolis doeste` | MT | geolocation | 2 | Figueirópolis D'Oeste | 0.97 |
| `grão pará` | SC | geolocation | 2 | Grão-Pará | 0.94 |
| `itapecuru-mirim` | MA | geolocation | 2 | Itapecuru Mirim | 0.97 |
| `limeira d oeste` | MG | geolocation | 2 | Limeira do Oeste | 0.96 |
| `machadinho d oeste` | RO | geolocation | 2 | Machadinho D'Oeste | 0.97 |
| `olho d agua das cunhas` | MA | geolocation | 2 | Olho d'Água das Cunhãs | 0.97 |
| `olho-d agua do borges` | RN | geolocation | 2 | Olho d'Água do Borges | 0.94 |
| `olho-d'água do borges` | RN | geolocation | 2 | Olho d'Água do Borges | 0.97 |
| `palmeira doeste` | SP | geolocation | 2 | Palmeira d'Oeste | 0.97 |
| `panema` | PR | geolocation | 2 | Capanema | 0.86 |
| `perola doeste` | PR | geolocation | 2 | Pérola d'Oeste | 0.96 |
| `pindaré mirim` | MA | geolocation | 2 | Pindaré-Mirim | 0.96 |
| `santa rita d oeste` | SP | geolocation | 2 | Santa Rita d'Oeste | 0.97 |
| `santo antônio do leverger` | MT | geolocation | 2 | Santo Antônio de Leverger | 0.95 |
| `sao joao d alianca` | GO | geolocation | 2 | São João d'Aliança | 0.97 |
| `sao joao do pau dalho` | SP | geolocation | 2 | São João do Pau d'Alho | 0.97 |
| `senador la roque` | MA | geolocation | 2 | Senador La Rocque | 0.97 |
| `angra dos reis rj` | RJ | sellers | 1 | Angra dos Reis | 0.92 |
| `ao bernardo do campo` | SP | sellers | 1 | São Bernardo do Campo | 0.97 |
| `auriflama/sp` | SP | sellers | 1 | Auriflama | 0.86 |
| `balenario camboriu` | SC | sellers | 1 | Balneário Camboriú | 0.94 |
| `belo horizont` | MG | sellers | 1 | Belo Horizonte | 0.96 |
| `brasilia df` | DF | sellers | 1 | Brasília | 0.89 |
| `cariacica / es` | ES | sellers | 1 | Cariacica | 0.86 |
| `cascavael` | PR | sellers | 1 | Cascavel | 0.94 |
| `floranopolis` | SC | sellers | 1 | Florianópolis | 0.96 |
| `garulhos` | SP | sellers | 1 | Guarulhos | 0.94 |
| `ji parana` | RO | sellers | 1 | Ji-Paraná | 0.94 |
| `juzeiro do norte` | CE | sellers | 1 | Juazeiro do Norte | 0.97 |
| `mogi das cruses` | SP | sellers | 1 | Mogi das Cruzes | 0.92 |
| `mogi das cruzes / sp` | SP | sellers | 1 | Mogi das Cruzes | 0.90 |
| `paincandu` | PR | sellers | 1 | Paiçandu | 0.94 |
| `ribeirao pretp` | SP | sellers | 1 | Ribeirão Preto | 0.92 |
| `riberao preto` | SP | sellers | 1 | Ribeirão Preto | 0.96 |
| `robeirao preto` | SP | sellers | 1 | Ribeirão Preto | 0.92 |
| `s jose do rio preto` | SP | sellers | 1 | São José do Rio Preto | 0.94 |
| `sando andre` | SP | sellers | 1 | Santo André | 0.90 |
| `sao bernardo do capo` | SP | sellers | 1 | São Bernardo do Campo | 0.97 |
| `sao jose do rio pret` | SP | sellers | 1 | São José do Rio Preto | 0.97 |
| `sao jose dos pinhas` | PR | sellers | 1 | São José dos Pinhais | 0.97 |
| `sao miguel d'oeste` | SC | sellers | 1 | São Miguel do Oeste | 0.94 |
| `sao paluo` | SP | sellers | 1 | São Paulo | 0.88 |
| `sao paulo sp` | SP | sellers | 1 | São Paulo | 0.89 |
| `sao paulop` | SP | sellers | 1 | São Paulo | 0.94 |
| `sao pauo` | SP | sellers | 1 | São Paulo | 0.93 |
| `sao sebastiao da grama/sp` | SP | sellers | 1 | São Sebastião da Grama | 0.93 |
| `scao jose do rio pardo` | SP | sellers | 1 | São José do Rio Pardo | 0.97 |
| `tabao da serra` | SP | sellers | 1 | Taboão da Serra | 0.96 |
| `...arraial do cabo` | RJ | geolocation | 1 | Arraial do Cabo | 0.90 |
| `alta floresta doeste` | RO | geolocation | 1 | Alta Floresta D'Oeste | 0.97 |
| `alvorada do oeste` | RO | geolocation | 1 | Alvorada D'Oeste | 0.93 |
| `amparo de sao francisco` | SE | geolocation | 1 | Amparo do São Francisco | 0.95 |
| `aparecida doeste` | SP | geolocation | 1 | Aparecida d'Oeste | 0.97 |
| `balneario de picarras` | SC | geolocation | 1 | Balneário Piçarras | 0.94 |
| `barão de monte alto` | MG | geolocation | 1 | Barão do Monte Alto | 0.94 |
| `belo horizonta` | MG | geolocation | 1 | Belo Horizonte | 0.92 |
| `buritirama` | MA | geolocation | 1 | Buritirana | 0.90 |
| `cachoeira de piria` | PA | geolocation | 1 | Cachoeira do Piriá | 0.94 |
| `campos dos goytacaze` | RJ | geolocation | 1 | Campos dos Goytacazes | 0.97 |
| `ceara mirim` | RN | geolocation | 1 | Ceará-Mirim | 0.95 |
| `figueirópolis doeste` | MT | geolocation | 1 | Figueirópolis D'Oeste | 0.97 |
| `franca sp` | SP | geolocation | 1 | Franca | 0.86 |
| `guarulhos-sp` | SP | geolocation | 1 | Guarulhos | 0.86 |
| `herval doeste` | SC | geolocation | 1 | Herval d'Oeste | 0.96 |
| `jaboatão dos gurarapes` | PE | geolocation | 1 | Jaboatão dos Guararapes | 0.98 |
| `jequiriçá` | BA | geolocation | 1 | Jiquiriçá | 0.89 |
| `lambari doeste` | MT | geolocation | 1 | Lambari D'Oeste | 0.96 |
| `lavras mg` | MG | geolocation | 1 | Lavras | 0.86 |
| `limeira do oeste mg` | MG | geolocation | 1 | Limeira do Oeste | 0.93 |
| `linharesl` | ES | geolocation | 1 | Linhares | 0.94 |
| `machadinho doeste` | RO | geolocation | 1 | Machadinho D'Oeste | 0.97 |
| `mujui dos campos` | PA | geolocation | 1 | Mojuí dos Campos | 0.93 |
| `muquem de sao francisco` | BA | geolocation | 1 | Muquém do São Francisco | 0.95 |
| `muquém de são francisco` | BA | geolocation | 1 | Muquém do São Francisco | 0.95 |
| `nova brasilandia doeste` | RO | geolocation | 1 | Nova Brasilândia D'Oeste | 0.98 |
| `olho dágua das cunhãs` | MA | geolocation | 1 | Olho d'Água das Cunhãs | 0.97 |
| `olho dágua grande` | AL | geolocation | 1 | Olho d'Água Grande | 0.97 |
| `olho-d'agua do borges` | RN | geolocation | 1 | Olho d'Água do Borges | 0.97 |
| `pau d  arco` | PA | geolocation | 1 | Pau D'Arco | 0.94 |
| `porto aelgre` | RS | geolocation | 1 | Porto Alegre | 0.91 |
| `rancho alegre d  oeste` | PR | geolocation | 1 | Rancho Alegre D'Oeste | 0.97 |
| `rio bracnco` | AC | geolocation | 1 | Rio Branco | 0.95 |
| `rio janeiro` | RJ | geolocation | 1 | Rio de Janeiro | 0.91 |
| `santa bárbara d`oeste` | SP | geolocation | 1 | Santa Bárbara d'Oeste | 0.95 |
| `santa rita doeste` | SP | geolocation | 1 | Santa Rita d'Oeste | 0.97 |
| `sao joao dalianca` | GO | geolocation | 1 | São João d'Aliança | 0.97 |
| `taliandia` | PA | geolocation | 1 | Tailândia | 0.89 |
| `venda nova do imigrante-es` | ES | geolocation | 1 | Venda Nova do Imigrante | 0.93 |
| `vila bela da santssima trindade` | MT | geolocation | 1 | Vila Bela da Santíssima Trindade | 0.98 |
| `xangrila` | RS | geolocation | 1 | Xangri-lá | 0.94 |

---

## Section 4 — Matched via ViaCEP

147 pairs were unresolved after tiers 1–3 but the most common associated
zip code returned a valid result from ViaCEP. The official localidade and UF are recorded.

| Raw city | State | Sources | Affected rows | ViaCEP localidade | ViaCEP UF | CEP used |
|---|---|---|---|---|---|---|
| `embu` | SP | customers, geolocation | 333 | Embu das Artes | SP | 06826-000 |
| `parati` | RJ | customers, geolocation | 196 | Paraty | RJ | 23970-000 |
| `bom jesus` | GO | customers, geolocation | 75 | Bom Jesus de Goiás | GO | 75570-000 |
| `acu` | RN | customers, geolocation | 58 | Açu | RN | 59650-000 |
| `goitacazes` | RJ | customers, geolocation | 55 | Campos dos Goytacazes | RJ | 28110-000 |
| `vila muriqui` | RJ | customers, geolocation | 47 | Mangaratiba | RJ | 23870-000 |
| `santa cecilia de umbuzeiro` | PB | geolocation | 37 | Campina Grande | PB | 58430-000 |
| `samambaia` | DF | geolocation | 19 | Brasília | DF | 72306-000 |
| `nossa senhora de caravaggio` | SC | customers, geolocation | 18 | Nova Veneza | SC | 88868-000 |
| `açu` | RN | geolocation | 17 | Açu | RN | 59650-000 |
| `itabatan` | BA | customers, geolocation | 15 | Mucuri | BA | 45936-000 |
| `picarras` | SC | customers, geolocation, sellers | 11 | Balneário Piçarras | SC | 88380-000 |
| `quatro bocas` | PA | customers, geolocation | 11 | Tomé-Açu | PA | 68682-000 |
| `porto trombetas` | PA | customers, geolocation | 10 | Oriximiná | PA | 68275-000 |
| `lago norte` | DF | geolocation | 9 | Brasília | DF | 71515-000 |
| `hidreletrica tucurui` | PA | customers, geolocation | 8 | Tucuruí | PA | 68464-000 |
| `nucleo residencial pilar` | BA | customers | 8 | Jaguarari | BA | 48967-000 |
| `vitoria` | PR | customers, geolocation | 8 | Guarapuava | PR | 85139-000 |
| `sao luiz` | RR | geolocation | 8 | São Luiz | RR | 69370-000 |
| `colonia vitoria` | PR | customers, geolocation | 7 | Guarapuava | PR | 85139-000 |
| `sp` | SP | geolocation, sellers | 7 | São Paulo | SP | 04776-000 |
| `aparecida de monte alto` | SP | customers, geolocation | 6 | Monte Alto | SP | 15915-000 |
| `arraial d ajuda` | BA | customers, geolocation | 6 | Porto Seguro | BA | 45816-000 |
| `colonia castrolanda` | PR | customers, geolocation | 6 | Castro | PR | 84196-000 |
| `vila dos cabanos` | PA | customers, geolocation | 6 | Barcarena | PA | 68447-000 |
| `itabirinha de mantena` | MG | geolocation | 6 | Itabirinha | MG | 35280-000 |
| `sao valerio da natividade` | TO | geolocation | 6 | São Valério | TO | 77390-000 |
| `carajas` | PA | customers, geolocation | 5 | Parauapebas | PA | 68516-000 |
| `penedo` | RJ | customers, geolocation | 5 | Itatiaia | RJ | 27598-000 |
| `santana do sobrado` | BA | customers, geolocation | 5 | Casa Nova | BA | 47310-000 |
| `novo diamantino` | MT | geolocation | 5 | Diamantino | MT | 78402-000 |
| `ponte alta` | MG | geolocation | 5 | Uberaba | MG | 38106-000 |
| `barra do tarrachil` | BA | customers, geolocation | 4 | Chorrochó | BA | 48668-000 |
| `itamaraca` | PE | geolocation | 4 | Ilha de Itamaracá | PE | 53900-000 |
| `sao sebastiao` | DF | geolocation | 4 | Brasília | DF | 71692-000 |
| `ilha dos valadares` | PR | customers, geolocation | 3 | Paranaguá | PR | 83252-000 |
| `maioba` | MA | customers | 3 | Paço do Lumiar | MA | 65137-000 |
| `morro de sao paulo` | BA | customers, geolocation | 3 | Cairu | BA | 45428-000 |
| `salobro` | BA | customers, geolocation | 3 | Canarana | BA | 44892-000 |
| `curitiba` | SP | sellers | 3 | Curitiba | PR | 80240-000 |
| `sao paulo - sp` | SP | sellers | 3 | São Paulo | SP | 04007-000 |
| `barra do jacuipe` | BA | geolocation | 3 | Camaçari | BA | 42833-000 |
| `caruara` | SP | geolocation | 3 | Santos | SP | 11200-000 |
| `fortaleza do tabocao` | TO | geolocation | 3 | Tabocão | TO | 77708-000 |
| `harmonia` | PR | geolocation | 3 | Telêmaco Borba | PR | 84275-000 |
| `hidrelétrica tucuruí` | PA | geolocation | 3 | Tucuruí | PA | 68464-000 |
| `pipa` | RN | geolocation | 3 | Tibau do Sul | RN | 59179-000 |
| `santo amaro` | MA | geolocation | 3 | Santo Amaro do Maranhão | MA | 65195-000 |
| `sao jorge do tiradentes` | ES | geolocation | 3 | Rio Bananal | ES | 29925-000 |
| `sao miguel de touros` | RN | geolocation | 3 | São Miguel do Gostoso | RN | 59585-000 |
| `colonia jordaozinho` | PR | customers | 2 | Guarapuava | PR | 85138-000 |
| `jardim abc de goias` | GO | customers, geolocation | 2 | Cidade Ocidental | GO | 72899-000 |
| `belo horizonte` | SP | sellers | 2 | Belo Horizonte | MG | 31160-000 |
| `caxias do sul` | SP | sellers | 2 | Caxias do Sul | RS | 95055-000 |
| `itajai` | SP | sellers | 2 | Itajaí | SC | 88301-000 |
| `rio de janeiro` | SP | sellers | 2 | Rio de Janeiro | RJ | 21320-000 |
| `rio de janeiro, rio de janeiro, brasil` | RJ | geolocation, sellers | 2 | Rio de Janeiro | RJ | 22793-000 |
| `4º centenario` | PR | geolocation | 2 | Quarto Centenário | PR | 87365-000 |
| `boa saude` | RN | geolocation | 2 | Boa Saúde | RN | 59260-000 |
| `chonim` | MG | geolocation | 2 | Governador Valadares | MG | 35109-000 |
| `colônia z-3` | RS | geolocation | 2 | Pelotas | RS | 96130-000 |
| `fortaleza do tabocão` | TO | geolocation | 2 | Tabocão | TO | 77708-000 |
| `itabatan (mucuri)` | BA | geolocation | 2 | Mucuri | BA | 45936-000 |
| `paranoa` | DF | geolocation | 2 | Brasília | DF | 71571-000 |
| `rio de janeiro` | AC | geolocation | 2 | Rio de Janeiro | RJ | 21550-000 |
| `santa efigenia` | MG | geolocation | 2 | Caratinga | MG | 35319-000 |
| `sousania` | GO | geolocation | 2 | Anápolis | GO | 75154-000 |
| `varzea nova` | PB | geolocation | 2 | Santa Rita | PB | 58304-000 |
| `alto sao joao` | PR | customers | 1 | Roncador | PR | 87323-000 |
| `caldas do jorro` | BA | customers | 1 | Tucano | BA | 48793-000 |
| `cuite velho` | MG | customers | 1 | Conselheiro Pena | MG | 35242-000 |
| `morada nova` | PA | customers | 1 | Marabá | PA | 68514-000 |
| `pitanga de estrada` | PB | customers | 1 | Mamanguape | PB | 58286-000 |
| `poco de pedra` | RN | customers | 1 | São Gonçalo do Amarante | RN | 59299-000 |
| `polo petroquimico de triunfo` | RS | customers | 1 | Triunfo | RS | 95853-000 |
| `04482255` | RJ | sellers | 1 | Rio de Janeiro | RJ | 22790-000 |
| `arraial d'ajuda (porto seguro)` | BA | sellers | 1 | Porto Seguro | BA | 45816-000 |
| `blumenau` | SP | sellers | 1 | Blumenau | SC | 89052-000 |
| `carapicuiba / sao paulo` | SP | sellers | 1 | Carapicuíba | SP | 06311-000 |
| `chapeco` | SP | sellers | 1 | Chapecó | SC | 89803-000 |
| `florianopolis` | SP | sellers | 1 | Florianópolis | SC | 88075-000 |
| `goioere` | SP | sellers | 1 | Goioerê | PR | 87360-000 |
| `ipira` | SP | sellers | 1 | Ipirá | BA | 44600-000 |
| `jacarei / sao paulo` | SP | sellers | 1 | Jacareí | SP | 12306-000 |
| `juiz de fora` | SP | sellers | 1 | Juiz de Fora | MG | 36010-000 |
| `lages - sc` | SC | sellers | 1 | Lages | SC | 88501-000 |
| `laguna` | SP | sellers | 1 | Laguna | SC | 88790-000 |
| `laranjeiras do sul` | SP | sellers | 1 | Laranjeiras do Sul | PR | 85301-000 |
| `londrina` | SP | sellers | 1 | Londrina | PR | 86076-000 |
| `maua/sao paulo` | SP | sellers | 1 | Mauá | SP | 09380-000 |
| `minas gerais` | MG | sellers | 1 | Campo do Meio | MG | 37165-000 |
| `palhoca` | SP | sellers | 1 | Palhoça | SC | 88136-000 |
| `parana` | PR | sellers | 1 | Maringá | PR | 87083-000 |
| `pinhais` | SP | sellers | 1 | Pinhais | PR | 83321-000 |
| `pinhais/pr` | PR | sellers | 1 | Pinhais | PR | 83327-000 |
| `porto alegre` | SP | sellers | 1 | Porto Alegre | RS | 91520-000 |
| `ribeirao preto / sao paulo` | SP | sellers | 1 | Ribeirão Preto | SP | 14079-000 |
| `rio bonito` | SP | sellers | 1 | Rio Bonito | RJ | 28810-000 |
| `rio de janeiro` | RN | sellers | 1 | Rio de Janeiro | RJ | 21210-000 |
| `rio de janeiro / rio de janeiro` | RJ | sellers | 1 | Rio de Janeiro | RJ | 20081-000 |
| `santa catarina` | SC | sellers | 1 | Palhoça | SC | 88135-000 |
| `santo andre/sao paulo` | SP | sellers | 1 | Santo André | SP | 09230-000 |
| `sao jose dos pinhais` | SP | sellers | 1 | São José dos Pinhais | PR | 83020-000 |
| `sao paulo / sao paulo` | SP | sellers | 1 | São Paulo | SP | 03407-000 |
| `sbc` | SP | sellers | 1 | São Bernardo do Campo | SP | 09861-000 |
| `sbc/sp` | SP | sellers | 1 | São Bernardo do Campo | SP | 09726-000 |
| `sertanopolis` | SP | sellers | 1 | Sertanópolis | PR | 86170-000 |
| `sp / sp` | SP | sellers | 1 | São Paulo | SP | 03363-000 |
| `tocantins` | SP | sellers | 1 | Tocantins | MG | 36512-000 |
| `vendas@creditparts.com.br` | PR | sellers | 1 | Maringá | PR | 87025-000 |
| `* cidade` | PR | geolocation | 1 | Curitiba | PR | 81470-000 |
| `4o. centenario` | PR | geolocation | 1 | Quarto Centenário | PR | 87365-000 |
| `amapari` | AP | geolocation | 1 | Pedra Branca do Amaparí | AP | 68945-000 |
| `antunes (igaratinga)` | MG | geolocation | 1 | Igaratinga | MG | 35698-000 |
| `aquidaban` | PR | geolocation | 1 | Marialva | PR | 86995-000 |
| `bh` | MG | geolocation | 1 | Belo Horizonte | MG | 31610-000 |
| `campo alegre de lourdes, bahia, brasil` | BA | geolocation | 1 | Campo Alegre de Lourdes | BA | 47220-000 |
| `campo grande` | RJ | geolocation | 1 | Rio de Janeiro | RJ | 23073-000 |
| `candangolandia` | DF | geolocation | 1 | Brasília | DF | 71727-000 |
| `colonia z-3` | RS | geolocation | 1 | Pelotas | RS | 96130-000 |
| `colônia vitória` | PR | geolocation | 1 | Guarapuava | PR | 85139-000 |
| `concordia de mucuri` | MG | geolocation | 1 | Ladainha | MG | 39826-000 |
| `cortado` | RS | geolocation | 1 | Novo Cabrais | RS | 96550-000 |
| `fatimarmnte dutra` | MA | geolocation | 1 | Presidente Dutra | MA | 65760-000 |
| `florian&oacute;polis` | SC | geolocation | 1 | Florianópolis | SC | 88058-000 |
| `floripa` | SC | geolocation | 1 | Florianópolis | SC | 88061-000 |
| `governador lomanto junior` | BA | geolocation | 1 | Barro Preto | BA | 45625-000 |
| `iauarete` | AM | geolocation | 1 | São Gabriel da Cachoeira | AM | 69790-000 |
| `itahum` | MS | geolocation | 1 | Dourados | MS | 79864-000 |
| `itamarati norte` | MT | geolocation | 1 | Campo Novo do Parecis | MT | 78361-000 |
| `lambari d%26apos%3boeste` | MT | geolocation | 1 | Lambari D'Oeste | MT | 78278-000 |
| `maceia³` | AL | geolocation | 1 | Maceió | AL | 57010-000 |
| `morro de são paulo` | BA | geolocation | 1 | Cairu | BA | 45428-000 |
| `nossa senhora da guia` | MT | geolocation | 1 | Cuiabá | MT | 78104-000 |
| `parati mirim` | RJ | geolocation | 1 | Paraty | RJ | 23972-000 |
| `penedo (itatiaia)` | RJ | geolocation | 1 | Itatiaia | RJ | 27598-000 |
| `praia grande (fundão) - distrito` | ES | geolocation | 1 | Fundão | ES | 29187-000 |
| `rj` | RJ | geolocation | 1 | Rio de Janeiro | RJ | 21341-000 |
| `roda velha` | BA | geolocation | 1 | São Desidério | BA | 47827-000 |
| `sao paulo` | AC | geolocation | 1 | São Paulo | SP | 04011-000 |
| `sbcampo` | SP | geolocation | 1 | São Bernardo do Campo | SP | 09780-000 |
| `são paulo` | RN | geolocation | 1 | São Paulo | SP | 02116-000 |
| `são valério da natividade` | TO | geolocation | 1 | São Valério | TO | 77390-000 |
| `tuiuti` | RS | geolocation | 1 | Bento Gonçalves | RS | 95710-000 |
| `vila marques` | MS | geolocation | 1 | Aral Moreira | MS | 79932-000 |
| `vitorinos - alto rio doce` | MG | geolocation | 1 | Alto Rio Doce | MG | 36264-000 |
| `várzea nova` | PB | geolocation | 1 | Santa Rita | PB | 58304-000 |

---

## Section 5 — No confident match

62 pairs remain unresolved after all four tiers.
These may be subdistricts, neighbourhoods, historical names, corrupt data, or
zip codes that return no result in ViaCEP.

| Raw city | State | Sources | Affected rows | Best fuzzy candidate | Score |
|---|---|---|---|---|---|
| `taguatinga` | DF | customers, geolocation | 85 | — | 0.22 |
| `primavera` | SP | customers, geolocation | 69 | — | 0.62 |
| `cruzeiro` | DF | geolocation | 47 | — | 0.25 |
| `ceilandia` | DF | customers, geolocation | 38 | — | 0.47 |
| `sobradinho` | DF | customers, geolocation | 31 | — | 0.44 |
| `guara` | DF | customers, geolocation | 29 | — | 0.31 |
| `japuiba` | RJ | customers, geolocation | 28 | — | 0.67 |
| `lago sul` | DF | geolocation | 22 | — | 0.27 |
| `catu de abrantes` | BA | customers, geolocation | 20 | — | 0.62 |
| `búzios` | RJ | geolocation | 15 | — | 0.55 |
| `santa maria` | DF | customers, geolocation | 14 | — | 0.33 |
| `ilha grande` | RJ | geolocation | 13 | — | 0.73 |
| `buzios` | RJ | geolocation | 11 | — | 0.55 |
| `piabeta` | RJ | geolocation | 10 | — | 0.57 |
| `gama` | DF | geolocation, sellers | 8 | — | 0.33 |
| `nucleo bandeirante` | DF | geolocation | 8 | — | 0.24 |
| `riacho fundo` | DF | geolocation | 5 | — | 0.32 |
| `planaltina de goias` | GO | customers, geolocation | 4 | — | 0.85 |
| `boa esperanca` | MT | geolocation | 4 | — | 0.77 |
| `planaltina` | DF | geolocation | 4 | — | 0.22 |
| `arembepe` | BA | customers, geolocation | 3 | — | 0.59 |
| `brazlandia` | DF | geolocation | 3 | — | 0.67 |
| `ceilândia` | DF | geolocation | 3 | — | 0.47 |
| `núcleo bandeirante` | DF | geolocation | 3 | — | 0.24 |
| `recanto das emas` | DF | geolocation | 3 | — | 0.36 |
| `luziapolis` | AL | customers, geolocation | 2 | — | 0.52 |
| `pau d'arco` | AL | customers, geolocation | 2 | — | 0.67 |
| `candangolândia` | DF | geolocation | 2 | — | 0.36 |
| `guará` | DF | geolocation | 2 | — | 0.31 |
| `vila sao francisco` | AL | geolocation | 2 | — | 0.52 |
| `jaua` | BA | customers | 1 | — | 0.75 |
| `aguas claras df` | SP | sellers | 1 | — | 0.67 |
| `andira-pr` | PR | sellers | 1 | — | 0.80 |
| `andradas` | SP | sellers | 1 | — | 0.82 |
| `bahia` | BA | sellers | 1 | — | 0.73 |
| `barbacena/ minas gerais` | MG | sellers | 1 | — | 0.60 |
| `castro pires` | MG | sellers | 1 | — | 0.70 |
| `centro` | MG | sellers | 1 | — | 0.62 |
| `marechal candido rondon` | PA | sellers | 1 | — | 0.48 |
| `marechal candido rondon` | SP | sellers | 1 | — | 0.54 |
| `novo hamburgo, rio grande do sul, brasil` | RS | sellers | 1 | — | 0.56 |
| `rio de janeiro \rio de janeiro` | RJ | sellers | 1 | — | 0.65 |
| `vila velha` | SP | sellers | 1 | — | 0.56 |
| `volta redonda` | SP | sellers | 1 | — | 0.61 |
| `bacaxa (saquarema) - distrito` | RJ | geolocation | 1 | — | 0.51 |
| `boa esperança` | MT | geolocation | 1 | — | 0.77 |
| `brazlândia` | DF | geolocation | 1 | — | 0.67 |
| `california da barra (barra do pirai)` | RJ | geolocation | 1 | — | 0.56 |
| `ceilandia norte` | DF | geolocation | 1 | — | 0.36 |
| `coqueiral` | ES | geolocation | 1 | — | 0.48 |
| `jacare (cabreuva)` | SP | geolocation | 1 | — | 0.67 |
| `jacaré (cabreúva)` | SP | geolocation | 1 | — | 0.67 |
| `japuíba` | RJ | geolocation | 1 | — | 0.67 |
| `macuco` | MG | geolocation | 1 | — | 0.62 |
| `monte gordo (camacari) - distrito` | BA | geolocation | 1 | — | 0.47 |
| `nova andradina` | RS | geolocation | 1 | — | 0.73 |
| `nova redencao bahia` | BA | geolocation | 1 | — | 0.83 |
| `realeza (manhuacu)` | MG | geolocation | 1 | — | 0.64 |
| `riacho fundo 2` | DF | geolocation | 1 | — | 0.30 |
| `são joão do pau d%26apos%3balho` | SP | geolocation | 1 | — | 0.76 |
| `são sebastião` | DF | geolocation | 1 | — | 0.50 |
| `tamoios (cabo frio)` | RJ | geolocation | 1 | — | 0.64 |
