# product sense 

- key question: how would we measure user churn on instagram


# AY iniial answer 
- while literal churn (account deletion exists), I'm not sure this is the actual business related metric we want. 
- In fact I'd want to know relative to what kind of actionable or what kind of remit/responsibilities exist for the teams that would use the metric for decisions/governance/reporting to really contextualize the problem.  
- generally taking an assumption that this for the generic product health performance of insta and not say specifically profitability or specific feature 
    - I might we're more approriately asking how often does a user drop below a critical usage threshold. And in the case to assume say "platform reachability" as our human threshold to define said threshold to be whether they've signed on at all and interacted with any feature (click, like, upload, DM) within the last 3 months. 
    - although the time frame of course is subject to any product/actionable spefics to be discovered that may affect what we think is the right time frame. 
    - this definition might also imply a "revival" rate that would be unrelated to user acquisition metrics 


# Video answer 

- Churn defined in terms of active users 
- interviewer wants to go through initial guiding approach for this
    - Instagram pretty broad, lots of features, any focus -- general users 
- Who is the stakeholder
    - executive viewpoint (a 1000 ft view?)
- User churn 
    - Inactive users
        - 
    - Drop is user engagement 


# SQL question - AY 

Q: user defined churned if they haven't displayed any active behavior in 7 days. How many uerss have churned as of today. 

table 
timestamp|user_id|activity 


- the one assumption for this question unclarified is what "today" means. When we say past 7 days if we're counting by the second, the window continues to move as we run the query throughout the day having different results and lack of reproducibility by day. 
- therefore by recommendation is to define for calculating only against the day and not timestamp 

- With only this table and no user table, we can only directly "see" who's active within the window and be forced to compare against itself (earlier to what window? full table?) 


-- for all time 
with active_users as (
    select distinct user_id
    from Usage 
    where datediff(current_date - timestamp) < 7)

select 
count(distinct user_id)

from Usage t1 
where user_id not in (select user_id from active_Users)