
# Look at M.E.  – Design Document

This document is intended to offer an insight glance at our service “Look at M.E.” from a user point of view.

Look at M.E. is a service that tries to collect data for the “Museum of Classical Arts” about the plaster replicas’ popularity among its visitors as well as offering a light-guided path for some of the rooms of the museum, illuminating their replicas sequentially, one after another, following a scheme based on a certain theme decided by the curator of the museum. So, the service will try to address the needs of both the visitors and the administrative branch of the museum.

We will begin with the personas we used to empathize with their needs, also, later denoting them through storyboards. Then, we will underline problems, or simply weaknesses that a regular visit to the Museum of Classical Arts of Sapienza could highlight. Finally, we will give a complete overview of Look at M.E.’s functionalities, implicitly presenting the solutions we applied to solve the issues.

# Personas

##  Monica
![Image of first persona](https://github.com/giovanniruocco/smartmuseum/blob/master/images/monica.png)

## Markus
![Image of second persona](https://github.com/giovanniruocco/smartmuseum/blob/master/images/markus.png)

## Lorenzo
![Image of third persona](https://github.com/giovanniruocco/smartmuseum/blob/master/images/lorenzo.png)

# Storyboards

What will follow next are the storyboards we used while designing Look at M.E.

The first story board represent the problem of indicating which artworks are the most popular.
![Image of first storyboard](https://github.com/giovanniruocco/smartmuseum/blob/master/images/1storyboard.png)
The second story board represent the user functionalities of Look at M.E.
![Image of second storyboard](https://github.com/giovanniruocco/smartmuseum/blob/master/images/2storyboard.png)

# Problems

## Popularity of the Artworks

At the moment, the museum is lacking a system that indicates the popularity of the replicas among its visitors. In particular, being able to learn such information, would help the administrative branch of the museum to have a better understanding of what attracts and pleases most of his customers. As a result, the administrative branch could use these notions to promote targeted advertising campaigns to increase the number of daily visitors. Also, it would be possible to obtain or, at least, borrow new artworks from other museums by exchanging them with less popular pieces which could be more appreciated in the other museums.

A possible solution could have been using personnel adhibited to this occupation, but this would be extremely inefficient in terms of resources and costs. So, it appears clear that an automatic system could be more advantageous from any point of view.

## Misfocusing

From a user point of view, the main issue that comes out is the risk of misfocusing when visiting a museum without any guidance. Indeed, whenever a visitor walks through the entrance unless he’s an expert in classical arts and knows very well the museum, what happens is that he might find himself not knowing where to start from, and, for instance, he might begin to examine a statue that is a reaching point for the artistical period it has been made. This would probably raise his expectations for the next sculptures he will see. So, moving to the next ones, since they are antecedents with respect to the first one, he might be left with a sense of disappointment.

Also, since having a lot of plaster statues he can examine, he might not be able to get a hold of them from a cultural point of view. Again, that happens because he might be thinking at the next ones he’d want to see after (he may be wondering about what will come next) and might not appreciate and focus on the one, he’s actually looking at, with the result of not liking both. This process could potentially lead to a sentiment of dissatisfaction while visiting the museum, and also, eventually, to not being able to enjoy the tour of the museum.

# Functionalities

We have divided this section into two parts, where the first one explains the features related to the visitors, while the second one is reserved for the direction of the museum.

Due to the profound differences between the two problems highlighted, even if it’s just one project, Look at M.E. can almost be considered as two systems combined, although independent between them. But we believe that gathering data about popularity, should also lead to involve more the neglected artworks through Look at M.E.’s user functionalities. This would potentially raise their value, therefore raising the value of the entire museum and lastly the quality of the entire user experience. That is why we have decided to carry on trying to solve both issues by creating a more complex service.

## User Functionalities

For the user, Look at M.E. creates a light-guided path that leads the visitors during their visit to the museum, enriching their experience with historical or artistic details.

Its functioning is the following. For the rooms chosen by the curators of the museum, the visitors may activate Look at M.E. through proximity sensors placed at the entrance of the rooms. Once activated, Look at M.E. will turn off the lights inside the room, and then illuminate the beginning artwork by the spotlights located near and pointing at it. At this point, a voice record will start playing, containing an explanation made by an expert of classical art. Once the recording is over, another piece is lighted, and its acoustic description broadcasted. This process will go on a loop until every replica is lightened up and explained. At this point, the lights of the room come back and Look at M.E. will go on standby, waiting for new visitors to start it again.

## Administrative Branch Functionalities

Look at M.E. also intends to provide valid support to the administrative branch of the museum by retrieving data on the habits of its customers. In particular, Look at M.E. will try to monitor through proximity sensors placed near the statues, how many visitors approximately examine each replica. Moreover, Look at M.E. will keep track of how long the proximity sensors will sense someone close to the statue. This system will supply values that are an estimator of the artworks’ popularity. For further details about the quality of the collected data, consult the document “Evaluation”.
