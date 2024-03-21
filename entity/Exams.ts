import { Entity, Column, PrimaryGeneratedColumn } from "typeorm"

@Entity()
export class Exams {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    criteria!: {
        question: string,
        test_ability: string,
    };

    @Column()
    graded_exams!: [number];
}


Teacher - id, surname, name, classes, email
Students - id, surname, name, img_name, class, teachers, parents_mail, exams, personal_rating
Student_class - id, students, classes
Exams - id, subject, date, teacher, 
Exams_criteria - id, 