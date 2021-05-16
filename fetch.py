from howdoi import howdoi
import asyncio

async def hdi(query):
    parser =  howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))
    output =  howdoi.howdoi(args)
    return(output)   

if __name__ == "__main__":
    print("Enter value to search")
    query = input()
    print(asyncio.run(hdi(query)))

